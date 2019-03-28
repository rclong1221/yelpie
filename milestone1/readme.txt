# Exercise 1: Parser
Code of CptS451_Online_parseJSON.py which was downloaded and used with files
in same directory as directed.

# Exercise 2: ER Diagram
Any of the RouthanaLong_ER_v1.<file_type> files will open the ER diagram.
I have the unpaid version of eDraw Max so the PDF file has a big watermark.
The SVG file might be easier to view and does not have the watermark.
RouthanaLong_relations_v1.sql is of the SQL statements.

# Exercise 3: Simple database app (web)

## Install dependencies 
pip install flask
pip install psycopg2

## Update database connection credentials in server.py line 6
conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' port='5433' password='password'")

## Run server
python server.py

## To use app, open a browser and navigate to:
http://127.0.0.1:5000/

