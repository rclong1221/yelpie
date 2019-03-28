from flask import Flask, jsonify, render_template, request
import psycopg2
app = Flask(__name__, template_folder='.', static_url_path='')

try:
    conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' port='5433' password='y33lilboy'")
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
        FROM business
        ORDER BY state;
    '''
    cursor.execute(q)
    l = cursor.fetchall()
    # l = ['state0', 'state1', 'state2', 'state3', 'state4']
    return jsonify({'states': l})

@app.route('/api/v1.0/cities/<string:state>/', methods=['GET'])
def read_cities(state):
    # Use state to make query
    q = '''
        SELECT DISTINCT city
        FROM business
        WHERE state='%s'
        ORDER BY city;
    ''' % state
    cursor.execute(q)
    c = cursor.fetchall()
    return jsonify({'cities': c})

@app.route('/api/v1.0/businesses/<string:state>/<string:city>/')
def read_businesses(state, city):
    q = '''
        SELECT name
        FROM business
        WHERE city='%s' AND state='%s';
    ''' % (city, state)
    cursor.execute(q)
    b = cursor.fetchall()
    return jsonify({'businesses': b})

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
