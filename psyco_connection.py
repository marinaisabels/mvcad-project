import psycopg2
from psycopg2.extras import RealDictCursor


conn = psycopg2.connect("dbname=cad_mvcad user=postgres password=isabel01 host=localhost")
conn.autocommit = True

cursor = conn.cursor(cursor_factory=RealDictCursor)