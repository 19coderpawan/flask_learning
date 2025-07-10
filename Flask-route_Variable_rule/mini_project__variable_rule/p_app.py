from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
       maths=float(request.form['maths'])
       english=float(request.form['english'])
       science=float(request.form['science'])

       score=(maths+english+science)/3 
       return render_template('form.html',score=score)   

if __name__=="__main__":
    app.run(debug=True)
    