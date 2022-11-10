import pymysql


class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        password = ''
        database = 'reviews'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()


    def add_user_review(self, name, recipe, comment):
        sql = """insert into user_review (name, recipe,comment) values (%s, %s, %s)"""
        input_values = (name, recipe, comment)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_recipe_id = "select user_id from user_review order by user_id desc limit 1"
        self.cursor.execute(sql_new_recipe_id)
        new_recipe = self.cursor.fetchone()
        return new_recipe[0]

    def get_recipe(self, user_review_user_id=None, limit=None):
        all_ = []
        if user_review_user_id is None:
            sql = "SELECT * FROM user_review order by user_id desc"
            self.cursor.execute(sql)
            all_review = self.cursor.fetchall()
        else:
            sql = """Select * from user_review where user_id = %s"""
            input_values = (user_review_user_id,)
            self.cursor.execute(sql, input_values)
            all_review = self.cursor.fetchone()
        return all_review




