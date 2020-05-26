
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

class DoesNotExist(Exception):
    pass
class InvalidField(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class Student:
    mem=''
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score
    
    @classmethod
    def sum(cls,field,**kwargs):
        cls.mem='sum'
        x= Student.filter(field,**kwargs)
        return x
    
    @classmethod
    def avg(cls,field,**kwargs):
        cls.mem='avg'
        x= Student.filter(field,**kwargs)
        return x
        
    @classmethod
    def count(cls,field,**kwargs):
        #if field is None:
			
        cls.mem='count'
        x= Student.filter(field,**kwargs)
        return x
    
    @classmethod
    def min(cls,field,**kwargs):
        cls.mem='min'
        x= Student.filter(field,**kwargs)
        return x

    @classmethod
    def max(cls,field,**kwargs):
        cls.mem='max'
        x= Student.filter(field,**kwargs)
        return x
        
    
    @classmethod 
    def filter(cls,field,**kwargs):
        if field not in('student_id','name','age','score'):
            raise InvalidField
            
            
        for key,value in kwargs.items():
           cls.c=key
           cls.d=value
        e=key.split("__")
   
        if e[0] not in('student_id','name','age','score'):
            raise InvalidField
        
        
        if len(e)==1:
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {}='{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {}={}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
            
        elif e[1]=='lt':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {}<'{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {}<{}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        elif e[1]=='lte':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {}<='{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {}<={}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        elif e[1]=='gt':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {}>'{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {}>{}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        elif e[1]=='gte':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {}>='{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {}>={}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        elif e[1]=='neq':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {}!='{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {}!={}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        elif e[1]=='in':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {} in '{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {} in {}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        elif e[1]=='contains':
            if len(kwargs)>=1:
                sql_query="select {}({}) from Student where {} like '{}'".format(cls.mem,field,e[0],cls.d)
                obj=read_data(sql_query)
            else:
                sql_query="select * from Student where {} like {}".format(e[0],cls.d)
                obj=read_data(sql_query)
        
        return obj[0][0]


'''min_age = Student.min('age', age__gt=18, age__lt=21)
print(min_age)
'''
