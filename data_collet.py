#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os


def Welcome():
	print '''
********************************************************
* Author: Escape                                       *
* Date & Time: 2016-06-20 22:00:00                     *
* Description: data flow collect                       *
********************************************************
'''


def Help():
    print("Usage: ./data_collet.py [-init [env|mysql] [-catch [tcp|udp|icmp]] [-insert] [-look] [--help]")
	print("-init")
	print("     env")
	print(" 	mysql")
	print -catch
	print 	  tcp
	print 	  udp
	print 	  icmp
	print -insert
	print 	  <table name>
	print -look
	print 	  <table name>
	print --help
'''


def data_collect(sub1, sub2):
	if sub1 == '-init':
		if sub2 == 'env':
			print os.popen('bash ./scripts/init_mysqldb.sh').read()
		elif sub2 == 'mysql':
			print os.popen('bash ./scripts/init_mysqldb.sh').read()
			print os.popen('python ./scripts/create_db.py').read()
		else:
			print "Please thinking agina"
			sys.exit(0)
	elif sub1 == '-catch':
		if sub2 == 'tcp':
			print "Please press Ctrl+C end the project..."
			print os.popen('python ./scripts/catch_packet.py eth0 tcp > ./tmp.txt').read()
		elif sub2 == 'udp':
			print "Please press Ctrl+C end the project..."
			print os.popen('python ./scripts/catch_packet.py eth0 udp > ./tmp.txt').read()
		elif sub2 == 'icmp':
			print "Please press Ctrl+C end the project..."
			print os.popen('python ./scripts/catch_packet.py eth0 icmp > ./tmp.txt').read()
		else:
			print "Please thinking agina"
			sys.exit(0)
	elif sub1 == '-insert':
		if sub2:
			print os.popen('python ./scripts/insert_to_mysql.py '+sub2+'').read()
	elif sub1 == '-look':
		if sub2:
			print os.popen('python ./scripts/print_data.py '+sub2+'').read()
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

    Welcome()
    if len(sys.argv) == 2:
	    sub1 = sys.argv[1]
	    sub2 = sys.argv[2]
	    data_collect(sub1, sub2)
    else:
        Help()
        exit(-1)

