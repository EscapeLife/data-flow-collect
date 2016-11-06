#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import MySQLdb
import sys


print "Now, create datebase date_collect"

conn = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'data_collect'
	)

cursor = conn.cursor()



tablename = sys.argv[1]
print tablename

sql_create_table = "create table "+tablename+" ( source varchar(50), version int, header int, tos int, total int, id int, flags int, offset int, ttl int, protocol varchar(4), checksum int, data varchar(5000), primary key (id));"
print sql_create_table

try:
 	cursor.execute(sql_create_table)
 	conn.commit()
	print ">>> Create table is done. "
except Exception as e:
	print "Error: e"
	conn.rollback()



range_num = os.popen('cat /root/porject/test-2.7.6/data_collect/tmp.txt | grep \'^$\' | wc -l').read()
a = int(range_num)
print a

f = open("/root/porject/test-2.7.6/data_collect/tmp.txt")
iter_f = iter(f)

for i in range(a):
	source = iter_f.next()
	source = source.strip()
	print source

	version = iter_f.next()
	version = version.strip()
	print version

	header = iter_f.next()
	header = header.strip()
	print header

	tos = iter_f.next()
	tos = tos.strip()
	print tos

	total = iter_f.next()
	total = total.strip()
	print total

	id = iter_f.next()
	id = id.strip()
	print id

	flags = iter_f.next()
	flags = flags.strip()
	print flags

	offset = iter_f.next()
	offset = offset.strip()
	print offset

	ttl = iter_f.next()
	ttl = ttl.strip()
	print ttl

	protocol = iter_f.next()
	protocol = protocol.strip()
	print protocol

	checksum = iter_f.next()
	checksum = checksum.strip()
	print checksum

	data = ''
	tmp = iter_f.next()
	while(tmp != '\n'):
		tmp = tmp.strip()
		data = data + tmp
		tmp = iter_f.next()
	print data


	sql_insert = "insert into "+tablename+" values ('"+source+"', "+version+", "+header+", "+tos+", "+total+", "+id+", "+flags+", "+offset+", "+ttl+", '"+protocol+"', "+checksum+", '"+data+"');"
	print sql_insert

	try:
		cursor.execute(sql_insert)
		conn.commit()
		print ">>> Insert into date to mysql is done. "
	except Exception as e:
		print "Error: e"
		conn.rollback()


cursor.close()
conn.close()
