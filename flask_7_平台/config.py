# 数据库config配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'nlp_sql'
USERNAME = 'root'
PASSWORD = '000000'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "asdh1nkls45jhwd4po"

# 邮箱配置

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "3057989377@qq.com"
MAIL_PASSWORD = "rsngfshbqahmdhch"
MAIL_DEFAULT_SENDER = "3057989377@qq.com"
# MAIL_MAX_EMAILS =   默认为无
# MAIL_SUPPRESS_SEND =   app.testing
# MAIL_ASCII_ATTACHMENTS =   False
