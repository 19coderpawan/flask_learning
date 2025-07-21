from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

#route for form.
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return  render_template('student_form.html')
    else:
        name=request.form['name']
        branch=request.form['branch']

        new_student=Student_table(name=name,branch=branch)
        db.session.add(new_student)
        db.session.commit()
        # return f"Student {name} is registered"
        return redirect(url_for('home'))
        

#route to display name of student in home page.
@app.route("/",methods=["GET"])
def home():
    student_data=Student_table.query.all()
    return render_template('home.html',student_data=student_data)    

#route to edit the data of student.
@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id):
    student_data=Student_table.query.get_or_404(id)
    if request.method=="POST":
        student_data.name=request.form['name']
        student_data.branch=request.form['branch']
        db.session.commit()
        redirect(url_for('home'))
    return render_template('edit.html',student_data=student_data)

# Model(table) 
class Student_table(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    branch=db.Column(db.String(20),nullable=False)

    # It’s a special Python method:
    # ells Python how to display the object in interactive shell / print() / logs.
    # It’s purely for human-friendly debugging.
    # def __repr__(self):
    #     return f"<Student{self.name}>"
    


if __name__=="__main__":
    app.run(debug=True)