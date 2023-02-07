from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer


# create the extension
db = SQLAlchemy()
app = Flask(__name__)
# path for the database stored
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)



# model created for the Item database
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    # name =Column(String(30),nullable=True,unique =True)
    # price =Column(Integer,nullable=True)
    # barcode = Column(String(12),nullable=False,unique=True)
    # description = Column(String(1024),nullable=False,unique=True)

    

    


@app.route('/')
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    
    return render_template("market.html", items=items,items_name ="phone")

@app.route("/about/<username>")
def about_page(username):
    return f'This is the About Page for the user :{username}'

if __name__ == '__main__':
    with app.app_context():
       db.create_all()
    # app.run(debug=True)
    
    