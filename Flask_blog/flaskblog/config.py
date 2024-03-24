

class Config:
       SECRET_KEY = '9fe105976705a1f0251b875e669d4286'
       SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
       MAIL_SERVER = 'smtp.googlemail.com'
       MAIL_PORT = 587
       MAIL_USE_TLS = True
       MAIL_USERNAME = 'davidalibalio5@gmail.com'
       MAIL_PASSWORD = 'ezee kmia fjgj ahrb'




'''testing for my own server'''
'''app.config['MAIL_SERVER'] = 'mail.techwithdidasserver.site'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '_mainaccount@techwithdidasserver.site'
app.config['MAIL_PASSWORD'] = 'Didasalibaliodavid1#'
mail = Mail(app)'''