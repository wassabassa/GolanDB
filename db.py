import os
import pickle

"""
Usage:

from db import DB

database_name = DB("path to database file")

database_name.functions()
"""



class DB:
    def __init__(self,path):
        self.path=path
        if(os.path.exists(path) and os.path.isfile(path)): 
            f=open(self.path,"rb")
            self.dict=pickle.load(f)
            f.close()
        else:
            print("Not a valid path, creating new file with empty dictionary.")
            self.dict={}
            self.update_file()#update the file in the path


    def update(self,key,value):
        if key in self.dict:
            self.dict[key]=value
            self.update_file()
            print(f"Updated value of key '{key}' to: '{value}'")
        else:
            print("Key not found, use insert to add new key-value pair.")


    def insert(self, key, value): 
        if key not in self.dict:
            self.dict[key]=value
            self.update_file()
        else:
            print("Key already exists in the database, use update to update an exisiting key-value pair.")


    def delete(self, key):
        if key in self.dict:
            del(self.dict[key])
            self.update_file()
        else:
            print("Key does not exist in database.")


    def read(self, key):
        if key in self.dict:
            print(self.dict[key])
        else:
            print("Key does not exist in database.")

    def update_file(self):
        f=open(self.path,"wb")
        pickle.dump(self.dict,f)
        f.close()
