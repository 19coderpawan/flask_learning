from flask import Flask;

app=Flask(__name__)

#decorator.
@app.route('/',methods=['GET']) 
def home():
    return "hello world my name is pawan"

@app.route('/about',methods=['GET'])
def about():
    return "<h1>this is about page</h1>"

if __name__=="__main__":
    app.run(debug=True)