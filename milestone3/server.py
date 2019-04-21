from flask import Flask, jsonify, render_template, request
from urllib.parse import unquote
import psycopg2
app = Flask(__name__, template_folder='.', static_url_path='')

CREDENTIALS = "dbname='yelpdb' user='postgres' host='localhost' port='5433' password='y33lilboy'"

try:
    conn = psycopg2.connect(CREDENTIALS)
except:
    print("Unable to connect to database...")

cursor = conn.cursor()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/api/v1.0/states/', methods=['GET'])
def read_states():
    q = '''
        SELECT DISTINCT state
        FROM Business
        ORDER BY state;
    '''
    cursor.execute(q)
    l = cursor.fetchall()
    return jsonify({'states': l})

@app.route('/api/v1.0/cities/<string:state>/', methods=['GET'])
def read_cities(state):
    # Use state to make query
    q = '''
        SELECT DISTINCT city
        FROM Business
        WHERE state='%s'
        ORDER BY city;
    ''' % state
    cursor.execute(q)
    c = cursor.fetchall()
    return jsonify({'cities': c})

@app.route('/api/v1.0/zips/<string:state>/<string:city>/')
def read_zips(state, city):
    q = '''
        SELECT DISTINCT zip
        FROM Business
        WHERE city='%s' AND state='%s'
        ORDER BY zip;
    ''' % (city, state)
    cursor.execute(q)
    b = cursor.fetchall()
    print(b)
    return jsonify({'zips': b})

@app.route('/api/v1.0/businesses/<string:state>/<string:city>/<string:zip>')
def read_businesses(state, city, zip):
    q = '''
        SELECT DISTINCT
          name,
          address,
          city,
          CAST(ROUND(stars::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(review_count::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(avg_rating::NUMERIC, 2) AS FLOAT),
          num_checkins
        FROM Business
        WHERE city='%s' AND state='%s' AND zip='%s'
        ORDER BY name;
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'businesses': b})

@app.route('/api/v1.0/filtered-businesses/<string:state>/<string:city>/<string:zip>/<string:categories>')
def read_filtered_businesses(state, city, zip, categories):
    c = unquote(categories)
    cats = "'" + c.replace("&A&", "', '") + "'"
    q = '''
        SELECT DISTINCT
          name,
          address,
          city,
          CAST(ROUND(stars::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(review_count::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(avg_rating::NUMERIC, 2) AS FLOAT),
          num_checkins
        FROM Business
        JOIN HasTypes ON Business.business_id=HasTypes.business_id
        WHERE city='%s' AND state='%s' AND zip='%s' AND category_name IN (%s)
        ORDER BY name;
    ''' % (city, state, zip, cats)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'businesses': b})

@app.route('/api/v1.0/categories/<string:state>/<string:city>/<string:zip>')
def read_categories(state, city, zip):
    q = '''
        SELECT DISTINCT category_name
        FROM Business
        JOIN HasTypes ON Business.business_id=HasTypes.business_id
        WHERE city='%s' AND state='%s' AND zip='%s'
        ORDER BY category_name;
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'categories': b})

@app.route('/api/v1.0/stats/<string:state>/<string:city>/<string:zip>')
def read_stats(state, city, zip):
    q = '''
        SELECT
          COUNT(business_id) AS total_businesses,
          CAST(AVG(population) AS INTEGER) AS population,
          CAST(AVG(mean_income) AS INTEGER) AS income
        FROM Census
        JOIN Business ON Census.zip=Business.zip
        WHERE Business.city='%s' AND Business.state='%s' AND Census.zip='%s';
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'stats': b})

@app.route('/api/v1.0/cat-stats/<string:state>/<string:city>/<string:zip>')
def read_cat_stats(state, city, zip):
    q = '''
        SELECT
          COUNT(HasTypes.business_id) AS total_businesses,
          category_name
        FROM Business
        JOIN HasTypes ON Business.business_id=HasTypes.business_id
        WHERE city='%s' AND state='%s' AND zip='%s'
        GROUP BY category_name
        ORDER BY category_name;
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'stats': b})

@app.route('/api/v1.0/expensive/<string:state>/<string:city>/<string:zip>')
def read_expensive_businesses(state, city, zip):
    q = '''
        SELECT DISTINCT
          Business.name,
          CAST(ROUND(Business.stars::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(Business.review_count::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(Business.avg_rating::NUMERIC, 2) AS FLOAT),
          Business.price
        FROM Business
        JOIN ( SELECT DISTINCT
            Business.business_id,
            MAX(higher_price) AS h_price
          FROM Business
          JOIN (
            SELECT
              B.business_id,
              (CASE WHEN B.price>avg_price THEN 1 ELSE 0 END) AS higher_price
            FROM Business AS B
            JOIN (
              SELECT
                category_name,
                zip,
                AVG(price) AS avg_price
              FROM Business
              JOIN HasTypes ON Business.business_id=HasTypes.business_id
              GROUP BY zip, category_name
            ) AS C ON B.zip=C.zip
          ) AS D ON Business.business_id=D.business_id
          WHERE city='%s' AND state='%s' AND zip='%s'
          GROUP BY Business.business_id
        ) AS Filtered ON Business.business_id=Filtered.business_id
        WHERE h_price=1
        ORDER BY Business.name;
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'expensive': b})

@app.route('/api/v1.0/popular/<string:state>/<string:city>/<string:zip>')
def read_popular_businesses(state, city, zip):
    q = '''
        SELECT DISTINCT
          Business.name,
          CAST(ROUND(Business.stars::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(Business.review_count::NUMERIC, 2) AS FLOAT),
          CAST(ROUND(Business.avg_rating::NUMERIC, 2) AS FLOAT)
        FROM Business
        JOIN ( SELECT DISTINCT
            Business.business_id,
            MAX(higher_rating) AS h_rating,
            MAX(higher_checkin) AS h_checkin,
            MAX(higher_revs) AS h_revs,
            MAX(higher_price) AS h_price
          FROM Business
          JOIN (
            SELECT
              B.business_id,
              (CASE WHEN B.avg_rating>avg_rate THEN 1 ELSE 0 END) AS higher_rating,
              (CASE WHEN B.num_checkins>avg_checkin THEN 1 ELSE 0 END) AS higher_checkin,
              (CASE WHEN B.review_count>avg_rev_count THEN 1 ELSE 0 END) AS higher_revs,
              (CASE WHEN B.price>avg_price THEN 1 ELSE 0 END) AS higher_price
            FROM Business AS B
            JOIN (
              SELECT
                category_name,
                zip,
                AVG(review_count) AS avg_rev_count,
                AVG(num_checkins) AS avg_checkin,
                AVG(avg_rating) AS avg_rate,
                AVG(price) AS avg_price
              FROM Business
              JOIN HasTypes ON Business.business_id=HasTypes.business_id
              GROUP BY zip, category_name
            ) AS C ON B.zip=C.zip
          ) AS D ON Business.business_id=D.business_id
          WHERE city='%s' AND state='%s' AND zip='%s'
          GROUP BY Business.business_id
        ) AS Filtered ON Business.business_id=Filtered.business_id
        WHERE h_checkin=1 AND h_revs=1
        ORDER BY Business.name;
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'popular': b})

@app.route('/api/v1.0/successful/<string:state>/<string:city>/<string:zip>')
def read_successful_businesses(state, city, zip):
    q = '''
        SELECT DISTINCT
          Business.name,
          CAST(ROUND(Business.review_count::NUMERIC, 2) AS FLOAT),
          Business.num_checkins
        FROM Business
        JOIN HasTypes ON Business.business_id=HasTypes.business_id
        JOIN (
          SELECT DISTINCT
            business_id,
            MAX(EXTRACT(EPOCH FROM review_date)) AS age
          FROM Review GROUP BY business_id
        ) AS A ON Business.business_id=A.business_id
        JOIN (
          SELECT
            category_name,
            zip,
            SUM(num_checkins) AS tot_checkins,
            CAST(ROUND(AVG(num_checkins)::NUMERIC, 2) AS FLOAT) AS avg_checkins,
            SUM(age) AS tot_age,
            CAST(ROUND(AVG(age)::NUMERIC, 2) AS FLOAT) AS avg_age
          FROM HasTypes
          JOIN Business ON HasTypes.business_id=Business.business_id
          JOIN (
            SELECT DISTINCT
              business_id,
              MAX(EXTRACT(EPOCH FROM review_date)) AS age
            FROM Review GROUP BY business_id
          ) AS A ON Business.business_id=A.business_id
          WHERE city='%s' AND state='%s' AND zip='%s'
          GROUP BY zip, category_name
        ) AS CatStats ON
          HasTypes.category_name=CatStats.category_name AND
          Business.zip=CatStats.zip
        WHERE
          Business.num_checkins > avg_checkins AND
          city='%s' AND
          state='%s' AND
          Business.zip='%s' AND
          (num_checkins / A.age) > (avg_checkins / avg_age)
        ORDER BY Business.name;
    ''' % (city, state, zip, city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'successful': b})

@app.route('/js/<path:path>/')
def get_js(path):
    print(path)
    return app.send_static_file(path)

@app.route('/css/<path:path>/')
def get_css(path):
    print(path)
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run()
