from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET']) 
def index():

    return render_template('index.html')
 
@app.route('/about',methods=['GET'])
def about():
    name=request.args.get('name','Guest')
    return render_template('about.html',name=name)

if __name__=="__main__":
    app.run(debug=True)



