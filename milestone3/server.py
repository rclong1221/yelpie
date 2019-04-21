from flask import Flask, jsonify, render_template, request
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
        WHERE city='%s' AND state='%s' AND zip='%s';
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'businesses': b})

@app.route('/api/v1.0/filtered-businesses/<string:state>/<string:city>/<string:zip>/<string:categories>')
def read_filtered_businesses(state, city, zip, categories):
    cats = "'" + categories.replace("&", "', '") + "'"
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
        WHERE city='%s' AND state='%s' AND zip='%s' AND category_name IN (%s);
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
        WHERE city='%s' AND state='%s' AND zip='%s';
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
        GROUP BY category_name;
    ''' % (city, state, zip)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'stats': b})

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
