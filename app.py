from flask import Flask;

app=Flask(__name__)

@app.route('/')
def home():
    return "hello world my name is pawan"

@app.route('/about')
def about():
    return "this is about page"

if __name__=="__main__":
    app.run(debug=True)