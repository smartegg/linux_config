#!/bin/sh
#
# script to install MySQL 5.5.10
#

#tar zxfv mysql-5.5.10.tar.gz
cd $1
# mysql-5.5.10

rm -fr CMakeCache.txt

cmake . \
-DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
-DMYSQL_DATADIR=/usr/local/mysql/data \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DMYSQL_TCP_PORT=3306 \
-DMYSQL_UNIX_ADDR==/tmp/mysql.sock \
-DMYSQL_USER=mysql \
-DWITH_DEBUG=1 \
-DUSE_SYS_STL=1 \
-DHAVE_QUERY_CACHE=0 \
-DWITH_EMBEDDED_SERVER=1

make
sudo make install

#add by dw
sudo groupadd mysql

sudo useradd mysql -d /usr/local/mysql/data/mysql -s /sbin/nologin -g mysql

cd /usr/local

sudo chown -R mysql:mysql mysql

cd mysql
#pay attention to the dir you act:its in the installion dir of mysql, default installation dir is /usr/local/mysql
sudo ./scripts/mysql_install_db --user=mysql
sudo cp ./support-files/my-medium.cnf /etc/my.cnf
sudo cp ./support-files/mysql.server /etc/init.d/mysqld
sudo chmod 755 /etc/init.d/mysqld

#add by dw
#need start a mysql demon before change password
sudo ./bin/mysqld_safe &
sudo ./bin/mysqladmin -u root password '123'
sudo killall mysqld
sudo killall mysqld_safe #maybe produce error, but  no problem

#sudo chkconfig --add mysqld
sudo /etc/init.d/mysqld start


