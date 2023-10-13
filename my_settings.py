DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'triton',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'OPTIONS':{
        #     'init_command': 'SET sql_mods="STRICT_TRANS_TABLES"'
        # }
    }
}
SECRET_KEY = 'django-insecure-%yrvszh+ha#%m!ell+y+4h1jhr^b)ykoss%m7xs)d)^vq1yzb5'