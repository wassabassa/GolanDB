import os
import pickle

class DB:
    def __init__(self,path):
        if('''path exist'''):
            pass
        #receive path of pickle file with dictionary
        else:
            print("no")
            self.dict={}
            self.update_file()#update the file in the path

    def update(self,key,value):
        pass
    def insert(key,value):
        pass
    def delete(key):
        pass
    def read(key):
        pass

    def update_file(self):
        f=open(self.path,"wb")
        pickle.dump(self.dict,f)
        f.close()


if __name__=="__main__":
    print("start")
    d=DB(r"c:\test\123.qqq")