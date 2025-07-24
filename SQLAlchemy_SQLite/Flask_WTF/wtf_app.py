from flask import Flask,request,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from form import EmployeeForm
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY'] = 'mysecretkey'  # Required for CSRF

db=SQLAlchemy(app)

class Employee_table(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    department=db.Column(db.String(30),nullable=False)

#home route
@app.route('/',methods=['GET'])
def home():
    emp_data=Employee_table.query.all()
    return render_template('home.html',emp_data=emp_data)

@app.route('/add',methods=['GET','POST'])
def add():
    form=EmployeeForm()
    if form.validata_on_submit():
        emp_record=Employee_table(name=form.name.data,department=form.department.data)
        db.session.add(emp_record)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')
    
        

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit():
    pass

@app.route('/delete/<int:id>',methods=['POST'])
def delete():
    emp_data=Employee_table.query.get_or_404(id)
    db.session.delete(emp_data)
    db.session.commit()
    return redirect(url_for('home'))



if __name__=="__main__":
    app.run(debug=True)