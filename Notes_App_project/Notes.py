from flask import Flask,redirect,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,DateField
from wtforms.validators import DataRequired
from datetime import date

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='pawankushwaha'

db=SQLAlchemy(app)

class Notes_Table(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(100),nullable=False)
    Content=db.Column(db.Text,nullable=False)
    Date=db.Column(db.Date,nullable=False,default=date.today)

class Notes_Form(FlaskForm):
    Date=DateField('Date',format='%Y-%m-%d',default=date.today,validators=[DataRequired()])
    Title=StringField('Title',validators=[DataRequired()])
    Content=TextAreaField('Content',validators=[DataRequired()])
    Submit=SubmitField('Submit')


@app.route('/',methods=['GET'])
def home():
    data=Notes_Table.query.all()
    return render_template('home.html',data=data)   

@app.route('/add',methods=['GET','POST'])
def add():
    form=Notes_Form()
    if form.validate_on_submit():
        new_data=Notes_Table(Title=form.Title.data,Content=form.Content.data,Date=form.Date.data)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template('Add_notes.html',form=form)

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    data_form=Notes_Table.query.get_or_404(id)
    form=Notes_Form(obj=data_form)
    if form.validate_on_submit():
        data_form.Date=form.Date.data
        data_form.Title=form.Title.data
        data_form.Content=form.Content.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_notes.html',form=form)

@app.route('/delete/<int:id>')
def delete(id):
    data=Notes_Table.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('home'))

    
 

   







if __name__=="__main__":
    app.run(debug=True)

