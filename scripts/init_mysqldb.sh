#! /bin/bash
# Author: Escape
# Date & Time: 2016-05-10 15:20:51
# Description:
# 		The first time install mysqldb and mysql-python.


# welcome
echo "###################################################################"
echo "#     Welcome, first time install mysqldb and mysql-python !      #"
echo "###################################################################"
echo



# install mysqldb
echo "##### Install mysqldb #####"
echo "[==        ]"
echo "[======    ]"

mysql --version || yum install -y mysql-server mysql mysql-deve >> /dev/null
if [ $? -ne 0 ]; then
	echo "Error: Install mysqldb is failed, please check..."
    exit 1
fi

echo "[==========]"
echo ">>> install mysqldb is done !"
echo



# install python for mysql
echo "##### install python for mysql #####"
yum install mysql-devel -y >> /dev/null
yum install MySQL-python -y >> /dev/null

wget http://nchc.dl.sourceforge.net/project/mysql-python/mysql-python/1.2.3/MySQL-python-1.2.3.tar.gz >> /dev/null
echo "[=         ]"

tar xvf MySQL-python-1.2.3.tar.gz >> /dev/null
echo "[==        ]"

cd MySQL-python-1.2.3 >> /dev/null
echo "[======    ]"

python setup.py install >> /dev/null
echo "[==========]"
echo ">>> install python for mysql is done !"
echo



# start mysql server
echo "##### start mysql server #####"
service mysqld restart >> /dev/null
echo "[==        ]"
echo "[======    ]"

netstat -anp | grep 3306 >> /dev/null
if [ $? -ne 0 ]; then
	echo "Error: Start mysql server is failed, please check..."
    exit 1
fi
	
echo "[==========]"
echo ">>> Start mysql server is done !"
echo



# init config
echo "##### Init config #####"
echo "[==        ]"
echo "[======    ]"
mysqladmin -u root password 'root' >> /dev/null
echo "[==========]"
echo ">>> Init config server is done !"



# stop mysql server
echo "##### stop mysql server #####"
echo "[==        ]"
echo "[======    ]"

service mysqld stop >> /dev/null
if [ $? -ne 0 ]; then
	echo "Error: Stop mysql server is failed, please check..."
    exit 1
fi
	
echo "[==========]"
echo ">>> Stop mysql server is done !"
echo



# Congratulates
echo "###################################################################"
echo "#      Congratulates you has completed the installment           #"
echo "###################################################################"
