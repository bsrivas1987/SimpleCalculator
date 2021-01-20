from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def calculate():
    result = ''
    operand = ''
    value1 = ''
    value2 = ''

    if request.method=='POST' and "val1" in request.form and "val2" in request.form and "calc" in request.form:
        value1 = float(request.form.get("val1"))
        value2 = float(request.form.get("val2"))

        if request.form.get("calc") == "Add":
            result = value1+value2
            operand = '+'
        elif request.form.get("calc")=="Subtract":
            result = value1-value2
            operand = '-'
        elif request.form.get("calc")=="Multiply":
            result = value1*value2
            operand = '*'
        elif request.form.get("calc")=="Divide":
            result = round(value1/value2, 2)
            operand = '/'
        else:
            result = 0

    return render_template("DataEntry.html", value1=value1, value2=value2, operand=operand, result=result)

app.run(host='localhost', port=5000)