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

        sql_new_user_review_user_id = "select user_id from user_review order by user_id desc limit 1"

        self.cursor.execute(sql_new_user_review_user_id)
        new_user_review = self.cursor.fetchone()
        return new_user_review[0]

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

    def add_user_recipe(self,user_name, rec_name, rec_ins):
        sql = """insert into user_recipe (user_name, rec_name, rec_ins) values (%s, %s, %s)"""
        input_values = (user_name, rec_name, rec_ins)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_user_recipe = "select ID from user_recipe order by ID desc limit 1"
        self.cursor.execute(sql_new_user_recipe)
        new_user_recipe = self.cursor.fetchone()
        return new_user_recipe[0]

    def geet_recipe(self, user_recipe_ID=None, limit=None):
        all_recipe = []
        if user_recipe_ID is None:
            sql = "SELECT * FROM user_recipe order by ID desc"
            self.cursor.execute(sql)
            all_recipe = self.cursor.fetchall()
        else:
            sql = """Select * from user_recipe where ID = %s"""
            input_values = (user_recipe_ID)
            self.cursor.execute(sql, input_values)
            all_recipe = self.cursor.fetchone()
        return all_recipe