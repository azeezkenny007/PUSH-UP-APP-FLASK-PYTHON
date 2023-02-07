from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer

app = Flask(__name__)
# path for the database stored
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' 
# To track modifications 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# model created for the Item database
class Item(db.Model):
    id = Column(Integer,primary_key=True)
    name =Column(String(30),nullable=True,unique =True)
    price =Column(Integer,nullable=True)
    barcode = Column(String(12),nullable=False,unique=True)
    description = Column(String(1024),nullable=False,unique=True)

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
    app.run()