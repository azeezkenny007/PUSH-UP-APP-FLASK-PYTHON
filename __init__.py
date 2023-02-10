from flask import Flask
from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,logout_user,login_required
from .models import User,session




db =SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]="secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
    
    db.init_app(app)
    login_manager =LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)
    
     
    @login_manager.user_loader
    def load_user(user_id):
        return session.query(User).get(int(user_id))
   
   

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
