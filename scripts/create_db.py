#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb


print '''
##################################
#        create databases        #
##################################
'''

conn = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root'
	)

cursor = conn.cursor()

sql_create_db = "create database data_collect"
sql_use_db = "use data_collect"


try:
	cursor.execute(sql_create_db)
	cursor.execute(sql_use_db)
	conn.commit()
	print "\n >>> Create date_collect db is done. \n"
except Exception as e:
	print "Error: e"
	conn.rollback()


cursor.close()
conn.close()
