import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


mydb=client['Employee']


information = mydb.emploteeinformation

record=[{
        'firstname':'John',
        'lastname':'Doe',
        'department':'Analytics',
        'qualification':'statistics',
        'age':35
        
        },
         {
        'firstname':'John ',
        'lastname':'Smith',
        'department':'Analytics',
        'qualification':'masters',
        'age':30
        
        },
        {
        'firstname':'Manish',
        'lastname':'Sen',
        'department':'Analytics',
        'qualification':'phd',
        'age':34
        
        },
        {
        'firstname':'Ram',
        'lastname':'Singh',
        'department':'Analytics',
        'qualification':'master',
        'age':32
        
        }]



# information.insert_one(record)
information.insert_many(record)