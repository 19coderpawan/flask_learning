from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

# Model(table) 
class Student_table(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    branch=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f"<Student{self.name}>"

if __name__=="__main__":
    app.run(debug=True)