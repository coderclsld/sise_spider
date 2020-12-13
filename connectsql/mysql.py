from flask_sqlalchemy import SQLAlchemy

dialect = 'mysql'
driver = 'pymysql'
username = 'root'
password = 'root'
database = 'liaotian'
host = '127.0.0.1'
port = '3306'
SQLALCHEMY_DATABASE_URI = \
    "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(dialect, driver, username, password, host, port, database)

db = SQLAlchemy()
