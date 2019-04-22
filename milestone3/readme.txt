# CPTS451 Project - Milestone 3

## Option 1: Updates via UPDATE (assigned)
Extract data to root directory of project
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
Extract data to root directory of project
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
