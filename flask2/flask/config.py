# общие настройки для нашего приложения
import os

SSL_CA_PATH = str('certs' / 'ca.crt')

db_host = os.environ.get("DATABASE_HOST")
db_port = os.environ.get("DATABASE_PORT")
db_user = os.environ.get("DATABASE_USER")
db_pass = os.environ.get("DATABASE_PASSWORD")
db_name = os.environ.get("DATABASE_NAME")


DATABASE_URI = f'mysql+pymysql://gen_user:GOGlmn3333$$$@496626cb628ae9919fbed983.twc1.net:3306/default_db'

SECRET_KEY = 'your_secret_key_here'