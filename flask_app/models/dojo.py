# import the functions that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

#model the class after the dojos table from dojos_and_ninjas_schema database
#create a list to add all the ninjas that associated with a dojo
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


#use class method to query database
#call the connectToMySQL function with the targeting schema
#create an empty list to append the instances
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_dojo = []
        for one_dojo in result:
            all_dojo.append(cls(one_dojo))
        return all_dojo


#class method to save all the dojos to the database
#return row number(ID) of the database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW());"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        return result


#class method to show individual dojo to the database
#return instance of the dojo object of the row number(ID)
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id =%(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo_with_ninjas = cls (results[0])
        print(dojo_with_ninjas)
        for row in results:
            ninja_data ={
                "id" : row['ninjas.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : row['ninjas.created_at'],
                "updated_at" : row['ninjas.updated_at']
            }
            dojo_with_ninjas.ninjas.append (Ninja( ninja_data))
        return dojo_with_ninjas


