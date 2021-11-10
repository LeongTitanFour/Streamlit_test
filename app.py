import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.cache to only run once.


@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    # return psycopg2.connect(**st.secrets["postgres"])
    return psycopg2.connect(host='localhost',
                            port='9900',
                            database='streamlit',
                            user='postgres',
                            password='titan4123')


conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.


@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * from username;")

# Print results.
# for row in rows:
#     print(row)
st.dataframe(data=rows)
# st.write(f"{row[0]} has a :{row[1]}:")
st.table(rows)

for a in rows:
    st.text(a[1])
