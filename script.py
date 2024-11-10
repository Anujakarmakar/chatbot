import psycopg

conn_info = "dbname=College user=postgres password=AnujaPostgres444 host=localhost port=5432"

conn = psycopg.connect(conn_info)
cur = conn.cursor()

# question = intput(_)
# query = gemini.get_response(context + question)

chat = '''
user: context question
gpt: query api
'''

# cur.execute(query)
# rows = cur.fetchall()

# ans = gemin.get_response(chat + rows)

# print(ans)
