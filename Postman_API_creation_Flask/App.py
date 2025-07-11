from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/api",methods=['POST'])
def test_api_calculate_sum():
    data=request.get_json()
    num1=float(dict(data)['num1'])
    num2=float(dict(data)['num2'])
    num3=float(dict(data)['num3'])

    return jsonify(num1+num2+num3)

if __name__=="__main__":
    app.run(debug=True)
