# Sparkify Song Play Analysis Database

## 1) Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

Sparkify runs one of the fastest growing music streaming services in the San Diego, CA, USA market. While the streaming app gathers usage data, it is not in a format that allows for analysis. This is a problem, as they want to analyze how users are actually listening to songs on the app. 

The purpose of this database is to allow for analysts and other users to be able run fast, intuitive queries on song play analysis. Examples of the type of queries Sparkify would like to know include: when do listeners listen the most during the day, which arists are the most popular, and do paid listeners listen more than free-tier users?


## 2) State and justify your database schema design and ETL pipeline.

The database is organized in what is considered a STAR schema, with different 'dimension' or attribute tables (i.e. artists, songs) tied to a central "fact" table that represents a transaction important to the business (i.e. songplays).

This format ensures data integrity, as attribute fields do not appear in more than one table. This means that when data needs to be updated, it only needs to be updated in one place. 

This format also simplifies the user queries, for example to see all the users, you would only need to execute ("SELECT * FROM users") to grab the users from the song table, rather than doing ("SELECT DISTINCT user_id,first_name,last_name,level FROM songplays"), if the user data was included in the songplays table in a denormalized format. 

One last benefit of this architecture is that it allows for fast aggregations. For example, to get the number of users one would have to execute (SELECT COUNT( * ) FROM users) instead of a query similar to the second one in the above paragraph. 

If query speed becomes an issue as the database grows and/or user needs change, the STAR format allows for the creation of denormalized tables, which would be optimized to the resepctive user query and greatly reduce downtime. 


## 3) Provide example queries and results for song play analysis.

##### Example 1: Total Songs by Weekday

To get the total number of songs played each weekday (Monday is 0 and Sunday is 6):
    
    '''
    SELECT time.weekday,COUNT( * ) AS n_plays FROM songplays 
    JOIN time ON songplays.start_time = time.start_time 
    GROUP BY time.weekday
    ORDER BY n_plays DESC;
    '''

The results would be something like this:

    weekday	count   
    2	1364
    4	1295
    1	1071
    3	1052
    0	1014
    5	628
    6	396

In this subset of the data, weekday 2 (Wednesday) is the day that had the most songplays.

##### Example 2: Total Songplays by Artist (Which artists are the most popular?)

To get the artists that had the most songplays:

    '''
    SELECT artists.name, COUNT( * ) as n_plays FROM songplays 
    JOIN artists ON songplays.artist_id = artists.artist_id 
    GROUP BY artists.name 
    ORDER BY n_plays DESC;
    '''

The results in this subset would be this:

    name	count
    Elena	1

This is due to the given subset of artists and songs mostly not appearing in the given log files.

### File Description

##### sql_queries.py:
This file contains all of the CREATE TABLE / INSERT queries needed to the create the tables and update them. 

##### create_tables.py:
Draws from the queries in sql_queries.py and actually creates the tables for the database, dropping them if they already exist. Note: if want to run, restart all kernels associated with the sparkifydb.

##### etl.py:
Draws from the insert queries in sql_queries.py to update each table. It parses through the data folders, song_data and log_data, processing each file and updating the requisite database.

##### etl.ipynb:
This notebook contains the workflow that was implemented in etl.py, with sections describing the etl process of each table. Note: when running create_tables.py, this kernel must be restarted if connected to the database.

##### test.ipynb:
This notebook serves as the file you can use to query and test that the database is actually populated, and populated correctly. Note: when running create_tables.py, this kernel must be restarted if connected to the database.

##### data:
Has 2 subfolders, log_data and song_data. These are a subset of Sparkify's user data.


### How to run the create_tables.py and etl.py scripts

There are a few options you have to run these scripts. 

In Jupyterlab, right click the .py file and select "Create Console for Editor", then select the desired python kernel. Next, highlight all code in the file you wish to execute (the whole file in this case) and press shift+enter to run.

An alternative would be using the Command Line/Terminal, navigating to your local python directory to get the executable, and dragging the file path from a File Explorer/Finder window. Ex: "python C:\Desktop\etl.py".

### How to create the database using these scripts

1. Run create_tables.py
2. Run etl.py


##### Created by Jacob Dodd