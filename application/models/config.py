import web

db_host = 's54ham9zz83czkff.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'afwefa7ho5scql18'
db_user = 'a8u98k2hrtlj36ww'
db_pw = 'uintca1zymqp2jbr'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )