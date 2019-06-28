# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (id SERIAL PRIMARY KEY, start_time timestamp NOT NULL,
    user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int NOT NULL, location varchar,user_agent varchar);
""") #would have song_id and artist_id be not null but in this case with a small subset of the data it wouldn't make sense

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, first_name varchar,
    last_name varchar, gender varchar, level varchar NOT NULL);
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar NOT NULL,
    artist_id varchar NOT NULL, year int, duration double precision);
""") # making title and artist_id have not null restraints as without it the info is useless.

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar,
    location varchar,lattitude double precision	,longitude double precision	);
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int,
    day int, week int, month int, year int, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (id, start_time,user_id, level, song_id,
    artist_id, session_id,location, user_agent)
    VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE
        SET level = CASE WHEN users.level != EXCLUDED.level
                         THEN EXCLUDED.level
                         ELSE users.level
                    END;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, lattitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT(start_time) DO NOTHING;
""")

# FIND SONGS

song_select = """
    SELECT songs.song_id, artists.artist_id FROM artists
    JOIN songs ON artists.artist_id = songs.artist_id 
    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;
"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]