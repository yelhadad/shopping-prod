# connect to postgres, the port is provided by default
# with keyword is for pretier syntax
import psycopg, os


print(os.environ['DBNAME'])
def get_db_connection():
    return psycopg.connect(
            dbname  =os.environ['DBNAME'],
            host    =os.environ['HOST'],
            user    =os.environ['USER'],
            password=os.environ['PASSWORD']
    )


# creates the users table, does nothing if the table exists
def create_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            email varchar (1000) NOT NULL,
            password varchar (1000) NOT NULL)
    """)
    conn.commit()
    cur.close()
    conn.close()


def create_shopping_table():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                    CREATE TABLE IF NOT EXISTS shopping(
                        id serial PRIMARY KEY,
                        product varchar (1000) NOT NULL,
                        quantity varchar (1000) NOT NULL,
                        user_id varchar (1000) NOT NULL)   
                        """)
            conn.commit()


def get_shopping_list():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM shopping")
            return cur.fetchmany()


def get_shopping_list_by_user_id(user_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""SELECT id,product, quantity FROM shopping WHERE user_id ='{user_id}'""")
            return cur.fetchall()


def insert_one_shopping(user_id, product, quantity):
    print(product, quantity, user_id)
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO shopping(user_id, product, quantity)
                            VALUES (%s, %s, %s)""", (user_id, product, quantity)
                        )
            conn.commit()


def change_one_shopping_product(item: dict, user_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            product = item['product']
            quantity = item['quantity']
            id = item['id']
            if quantity is None:
                cur.execute(f"""UPDATE shopping
                            SET product='{product}'
                            WHERE id='{id} AND user_id='{user_id}''""")
            elif product is None:
                cur.execute(f"""UPDATE shopping
                                SET product='{quantity}'
                                WHERE id='{id}' AND user_id='{user_id}'""")
            else:
                cur.execute(f"""UPDATE shopping
                                SET product='{product}', quantity='{quantity}'
                                WHERE id='{id}' AND user_id='{user_id}'""")
            conn.commit()

#not working!!!!
def delete_item(item_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""Select * FROM shopping WHERE id=%s""", (item_id))
            conn.commit()

def delete_item_by_id(id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM shopping WHERE id=%s", (id,))
            conn.commit()


def create_user(email, password):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO users(email, password)
                            VALUES (%s, %s)""",
                        (email, password))
            conn.commit()
            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
           # print(cur.description)
           # print(cur.fetchone())
            user = cur.fetchone()
            return user[0], user[1]


def get_user_by_id(id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id=%s", (id,))
        return cur.fetchone()


def get_user_by_email(email):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
            # print(cur.fetchone())
           # print(cur)
            return cur.fetchone()


def select_all_users():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            # print(cur.fetchone())
            return cur.fetchone()


def check_if_user_exists(email):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
           # print(cur.fetchone())
            if cur.fetchone() == None:
                return False
            else:
                return True


def q_create_users_table():
    return """
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            email varchar (1000) NOT NULL,
            password BINARY (100) NOT NULL)
    """


def q_create_user(email, password):
    return ("""INSERT INTO users(email, password)
                            VALUES (%s, %s)""",
                        (email, password))


def q_get_user_by_id(email):
    return """SELECT id FROM users"""






