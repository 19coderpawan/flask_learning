from flask import Flask

app=Flask(__name__)

@app.route("/home/<username>") # defining route variable in decorator.
def home(username): # here whatever value is in the <> brackets passed in the url dynamic part will be passed to fun.
    return f"Welcom to home page {username} " # this is how you access it .


if __name__=="__main__":
    app.run(debug=True)