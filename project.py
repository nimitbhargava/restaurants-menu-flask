from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/hello")
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
    
    