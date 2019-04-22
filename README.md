# yelpie

# CPTS451 Project - Milestone 2

## Exercise 1: Parser
Code of CptS451_Online_parseJSON.py which was downloaded and used with files
in same directory as directed.

## Exercise 2: ER Diagram
Any of the RouthanaLong_ER_v1.<file_type> files will open the ER diagram.
I have the unpaid version of eDraw Max so the PDF file has a big watermark.
The SVG file might be easier to view and does not have the watermark.
RouthanaLong_relations_v1.sql is of the SQL statements.

## Exercise 3: Simple database app (web)

### Install dependencies
pip install flask
pip install psycopg2

### Update database connection credentials in server.py line 6
conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' port='5433' password='password'")

### Run server
python server.py

### To use app, open a browser and navigate to:
http://127.0.0.1:5000/

# CPTS451 Project - Milestone 2

## Option 1: Updates via UPDATE (assigned)
### Extract data to root directory of project
1) Create and switch to database
2) Run statements from Routhana_Long_RELATIONS_v2.sql
3) Open a terminal and navigate to work directory
4) Install dependencies with "pip install flask psycopg2"
5) Update database connection at global variable "CREDENTIALS = ..."
6) Populate DB with "python parseAndInsert"
7) Run statements from Routhana_Long_UPDATES.sql
8) Run statements from Routhana_Long_INDEX.sql to create index
9) Run web server with "python server.py"
10) To view app, navigate to "http://127.0.0.1:5000/"

## Option 2: Updates via TRIGGERS
### Extract data to root directory of project
1) Create and switch to database
2) Run statements from Routhana_Long_RELATIONS_v2.sql
3) Run statements from Routhana_Long_TRIGGERS.sql
4) Open a terminal and navigate to work directory
5) Install dependencies with "pip install flask psycopg2"
6) Update database connection at global variable "CREDENTIALS = ..."
7) Populate DB with "python parseAndInsert"
8) Run statements from Routhana_Long_INDEX.sql to create index
9) Run web server with "python server.py"
10) To view app, navigate to "http://127.0.0.1:5000/"

## Writeup
Code in the writeup requires one of the above options be completed.
