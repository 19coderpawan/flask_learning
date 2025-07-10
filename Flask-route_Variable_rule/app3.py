from flask import Flask,request
import uuid

app=Flask(__name__)

# @app.route("/home/<username>") # defining route variable in decorator.
# def home(username): # here whatever value is in the <> brackets passed in the url dynamic part will be passed to fun.
#     return f"Welcom to home page {username} " # this is how you access it .
# another way-:
@app.route("/home")
def home():
    name=request.args.get('name','Guest') # for this the pattern is /home?name
    return f"hello {name} welcome to home page"

@app.route("/userage/<int:age>")
def userage(age):
    return f"your age is {age}"

@app.route("/name/<name>/age/<int:age>") # way to define multiple route variable.
def name(name,age):
    return f"your name is {name} and your age is {age} "
@app.route("/gen_uuid")
def gen_uuid():
    uid=uuid.uuid4()
    return f"the uuid is {uid}"


if __name__=="__main__":
    app.run(debug=True)