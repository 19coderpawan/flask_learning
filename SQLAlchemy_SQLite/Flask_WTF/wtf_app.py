from flask import Flask,request,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)

class Employee_table(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    department=db.Column(db.String(30),nullable=False)




if __name__=="__main__":
    app.run(debug=True)