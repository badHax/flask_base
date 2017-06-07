from app_name import app

database = {
    'TYPE' : 'postgresql+psycopg2',
    'USER' : None,
    'PASSWORD' : None,
    'HOST' : 'localhost',
    'DATABASE' : None
}
app.secret_key = 'IWHR020294041U23EN23H04914U49343U1CU1I313UC'
app.config['SQLALCHEMY_DATABASE_URI'] = database['TYPE']+'://'+database['USER']+\
    ':'+database['PASSWORD']+'@'+database['HOST']+'/'+database['DATABASE']