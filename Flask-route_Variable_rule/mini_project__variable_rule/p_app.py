from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/pass/<score>")
def Pass(score):
    return f"You passed the exam and your score is {score}"
    
@app.route("/fail/<score>")
def Fail(score):
    return f"You failed the exam and your score is {score}"


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
       maths=float(request.form['maths'])
       english=float(request.form['english'])
       science=float(request.form['science'])

       score=(maths+english+science)/3 
       res=""
       if score>=45:
           res="Pass"
       else:
           res="Fail" 

       return redirect(url_for(res,score=score))         

if __name__=="__main__":
    app.run(debug=True)
    