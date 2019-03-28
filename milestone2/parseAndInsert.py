import json
import psycopg2

CREDENTIALS = "dbname='yelpdb' user='postgres' host='localhost' port='5433' password='password'"

category_dict = dict()

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'

def parseAndInsertBusinesses():
    #reading the JSON file
    with open('./yelp_business.JSON','r') as f:    #TODO: update path for the input file
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        #TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect(CREDENTIALS)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            if count_line % 500 == 0: print("Business: parsed %i lines..." % (count_line))
            data = json.loads(line)

            attr = data["attributes"]
            price = "NULL"
            if "RestaurantsPriceRange2" in attr:
                price = attr["RestaurantsPriceRange2"]

            # Generate the INSERT statement for the cussent business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            sql_str = "INSERT INTO Business (business_id, name, address, state, city, zip, latlong, stars, review_count, num_checkins, open_status, price) " \
                      "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" + \
                      cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["city"]) + "','" + cleanStr4SQL(data["postal_code"]) + "',(POINT(" + str(data["latitude"]) + "," + \
                      str(data["longitude"]) + "))," + str(data["stars"]) + ",0,0,"  + \
                      int2BoolStr(data["is_open"]) + "," + str(price) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to Business table failed!")
                # print(sql_str)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # outfile.write(sql_str)

            # process business categories
            for category in data['categories']:
                if category not in category_dict:
                    category_dict[category] = 0

                    sql_str = "INSERT INTO Category (category_name) " \
                        "VALUES ('" + cleanStr4SQL(category) + "');"

                    try:
                        cur.execute(sql_str)
                    except:
                        print("Insert to Category table failed!")
                        # print(sql_str)
                    conn.commit()

                sql_str = "INSERT INTO HasTypes (business_id, category_name) " \
                          "VALUES ('" + cleanStr4SQL(data['business_id']) + "', '" + cleanStr4SQL(category) + "');"

                try:
                    cur.execute(sql_str)
                except:
                    print("Insert to HasTypes table failed!")
                    # print(sql_str)
                conn.commit()

            line = f.readline()
            count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def parseAndInsertCensus():
    #reading the JSON file
    with open('./zipData.csv','r') as f:    #TODO: update path for the input file
        line = f.readline()
        count_line = 0

        sql_str = None


        #connect to yelpdb database on postgres server using psycopg2
        #TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect(CREDENTIALS)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            if count_line % 500 == 0: print("Census: parsed %i lines..." % (count_line))
            if count_line > 0:
                line = line.replace(")", ");").replace(";,", ";").replace(".", "Null")
                sql_str = "INSERT INTO Census (zip, median_income, mean_income, population) VALUES " + line

                try:
                    cur.execute(sql_str)
                except:
                    print("Insert to Census table failed!")
                    print(sql_str)
                conn.commit()
                # optionally you might write the INSERT statement to a file.
                # outfile.write(sql_str)

            line = f.readline()
            count_line += 1

        cur.close()
        conn.close()

    print(count_line - 1)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def parseAndInsertUsers():
    #reading the JSON file
    with open('./yelp_user.JSON','r') as f:    #TODO: update path for the input file
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        #TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect(CREDENTIALS)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            if count_line % 500 == 0: print("Users: parsed %i lines..." % (count_line))
            data = json.loads(line)
            # Generate the INSERT statement for the cussent business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            sql_str = "INSERT INTO Users (user_id, user_name, yelping_since, fans, funny, useful, cool) " \
                      "VALUES ('" + cleanStr4SQL(data['user_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + str(data["yelping_since"]) + "','" + \
                      str(data["fans"]) + "'," + str(data["compliment_funny"]) + "," + str(data["useful"]) + "," + \
                      str(data["compliment_cool"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to Users table failed!")
                print(sql_str)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # outfile.write(sql_str)

            line = f.readline()
            count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def parseAndInsertReviews():
    #reading the JSON file
    with open('./yelp_review.JSON','r') as f:    #TODO: update path for the input file
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        #TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect(CREDENTIALS)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            if count_line % 500 == 0: print("Reviews: parsed %i lines..." % (count_line))
            data = json.loads(line)
            # Generate the INSERT statement for the cussent business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            sql_str = "INSERT INTO Review (review_id, business_id, user_id, review_date, review_text, cool, funny, useful, stars) " \
                      "VALUES ('" + cleanStr4SQL(data['review_id']) + "','" + cleanStr4SQL(data["business_id"]) + "','" + cleanStr4SQL(data["user_id"]) + "','" + \
                      str(data["date"]) + "','" + cleanStr4SQL(data["text"]) + "'," + str(data["cool"]) + "," + str(data["funny"]) + "," + \
                      str(data["useful"]) + "," + str(data["stars"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to Review table failed!")
                print(sql_str)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # outfile.write(sql_str)

            line = f.readline()
            count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def parseAndInsertCheckIns():
    #reading the JSON file
    with open('./yelp_checkin.JSON','r') as f:    #TODO: update path for the input file
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        #TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect(CREDENTIALS)
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            if count_line % 500 == 0: print("CheckIns: parsed %i lines..." % (count_line))
            data = json.loads(line)
            # Generate the INSERT statement for the cussent business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            sql_str = "INSERT INTO CheckIn (business_id, day, hour, amount) VALUES "

            for t, days in data.items():
                if t == "time":
                    for day, times in days.items():
                        for time, count in times.items():
                            sql_str +=  "('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(day) + "','" + cleanStr4SQL(time) + "'," + str(count) + "),"
            q = sql_str[:-1] + ";"
            try:
                cur.execute(q)
            except:
                print("Insert to CheckIn table failed!")
                print(q)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # outfile.write(sql_str)

            line = f.readline()
            count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

parseAndInsertCensus()
parseAndInsertBusinesses()
parseAndInsertUsers()
parseAndInsertReviews()
parseAndInsertCheckIns()
