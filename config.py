#博客基本配置

BLOG_NAME = 'Hello Blog'


# 数据库配置文件
SECRET_KEY = "ASNDAHDAHDAHD"
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'blog'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
