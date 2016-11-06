#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb


table = sys.argv[1]

conn = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'data_collect'
	)

cursor = conn.cursor()


sql_select_db = "select data from %s order by id, offset;" % table


try:
	cursor.execute(sql_select_db)
	conn.commit()
	print sql_select_db
	rs = cursor.fetchall()
	data = ''
	for row in rs:
		data = data + row[0] + ' '
	print data
except Exception as e:
	print "Error: "
	conn.rollback()


cursor.close()
conn.close()
