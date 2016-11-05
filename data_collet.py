#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os


def Welcome():
	print '''
##################################
#     weclome, data_collect !    #
##################################
'''


def Help():
	print '''
Option:
	-init
		env
		mysql
	-catch
		tcp
		udp
		icmp
	-insert
		<table name>
	-look
		<table name>
	--help
'''


def data_collect(sub1, sub2):
	if sub1 == '-init':
		if sub2 == 'env':
			print os.popen('bash ./init_mysqldb.sh').read()
		elif sub2 == 'mysql':
			print os.popen('bash ./init_mysqldb.sh').read()
			print os.popen('python ./create_db.py').read()
		else:
			print "Please thinking agina"
			sys.exit(0)
	elif sub1 == '-catch':
		if sub2 == 'tcp':
			print "Please press Ctrl+C end the project..."
			print os.popen('python ./catch_packet.py eth0 tcp > ./tmp.txt').read()
		elif sub2 == 'udp':
			print "Please press Ctrl+C end the project..."
			print os.popen('python ./catch_packet.py eth0 udp > ./tmp.txt').read()
		elif sub2 == 'icmp':
			print "Please press Ctrl+C end the project..."
			print os.popen('python ./catch_packet.py eth0 icmp > ./tmp.txt').read()
		else:
			print "Please thinking agina"
			sys.exit(0)
	elif sub1 == '-insert':
		if sub2:
			print os.popen('python ./insert_to_mysql.py '+sub2+'').read()
	elif sub1 == '-look':
		if sub2:
			print os.popen('python ./print_data.py '+sub2+'').read()
		else:
			print "Please thinking agina"
			sys.exit(0)
	elif sub1 == '--help':
		if sub2:
			Help()
	else:
		print "Please thinking agina"
		sys.exit(0)



if __name__ == '__main__':

	sub1 = sys.argv[1]
	sub2 = sys.argv[2]

	Welcome()
	data_collect(sub1, sub2)

