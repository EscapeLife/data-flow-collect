# data-flow-collect

![data-flow-collect](./images/index.jpg)

## Description information
> The project is based on python to achieve TCP, UDP and ICMP data flow reorganization to be able to restore the received TCP, UDP and ICMP content, to restore it.


## Scripts list
- **`[date-flow-collect]`**
- [x] **data_collect.py** - Execute the entry file
 - **`[scripts]`**
 - [x] **init_env.sh** - Installs MySQLdb database
 - [x] **init_mysqldb.sh** - Installs and creates the required the MySQLdb database and table information
 - [x] **create_db.py** - creates the required the MySQLdb database and table information
 - [x] **catch_packet.py** - Collects data flow information about TCP、UDP、ICMP
 - [x] **insert_to_mysql.py** - The information collected into the database for preservation
 - [x] **print_data.py** - Print data flow information, more IP protocol id value to sort
- [x] **LICENSE** - Apache License
- [x] **README.md** - readme.md

## Show results

