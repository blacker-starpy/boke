import sys, os
import pymysql


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 设置上传文件的路径

CLIENT_ID = 2234418481
APP_SECRET = '76daf2e9dxe4245d671x144154f55xc32150'

# 生成环境下才有效：
DEBUG = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('//','/')
MEDIA_URL = '/media/'
SITE_ID =1
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'boke',
        'USER': 'root',
        'PASSWORD': '155345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


USE_TZ = False