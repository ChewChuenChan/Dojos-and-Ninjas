# import the functions that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


#model the class after the ninjas table from dojos_and_ninjas_schema database
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#class method to save all the ninjas to the database, include the foreign key
#return row number(ID) of the database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas ( first_name, last_name, age ,created_at, updated_at, dojo_id ) VALUES ( %(first_name)s, %(last_name)s, %(age)s , NOW() , NOW(), %(dojo_id)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        return result