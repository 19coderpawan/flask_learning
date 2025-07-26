from flask import Flask,redirect,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='pawankushwaha'

db=SQLAlchemy(app)

class Notes_Table(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(100),nullable=False)
    Content=db.Column(db.Text,nullable=False)

   







if __name__=="__main__":
    app.run(debug=True)

