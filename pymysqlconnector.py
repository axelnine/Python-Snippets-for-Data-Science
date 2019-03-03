# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:39:31 2018

@author: PRESHAH
"""

import pymysql,sys,global_variable as gv
import pandas as pd

def connect():
    '''
    '''
    try:
        con = pymysql.connect(host=gv.host,user=gv.user, password=gv.password, db=gv.dbname)
    except Exception as e:
        print('Error in connecting to DB ',e)
    return con

def facebook(con):
    '''
    Input: takes in connection
    Output: Can vary according to requirements
    
    This function implements a couple of SQL queries by using the connection through pymysql library.
    '''
    cursor = con.cursor()
    
    #Select statements
    
    query = '''
            SELECT columns 
            FROM table 
            where conditions
            '''
    try:
        cursor.execute(query)
    except Exception as e:
        print('Error in query execution ',e)

    df = pd.DataFrame(list(cursor.fetchall()),columns=['columns'])

    if df.empty:
        return
    
    
    #Update statements
    
    for rows in df.itertuples():
        query1 = '''
                UPDATE table 
                SET `variable name`=%s
                where condition=%s'''
        try:
            cursor.execute(query1,(str(rows[1]),str(rows[2]),str(rows[3])))
        except Exception as e:
            print('Error in Updates query execution :', e)
            return None
        con.commit()
        
    print("Successfully executed")