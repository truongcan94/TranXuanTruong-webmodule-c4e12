from flask import Flask, render_template,redirect
app = Flask(__name__)




@app.route('/pratical2')
def pra2():
    return render_template("pratical2.html")




@app.route('/pratical1')
def pra1():
    return render_template("pratical1.html")




@app.route('/bmi/<w>/<h>')
def bmi(a, b):
    c = float (int(h)/100)
    BMI = int(w)/(c*c)
    if (BMI<16):
        return "<h1>You are severely underweight (còi xương)</h1>"
    elif (16 <=BMI <18.5):
        return "<h1>You are underweight (Thiếu cân)</h1> "
    elif (18.5<= BMI < 25):
        return "<h1>You are normal (Bình thường)</h1>"
    elif (25 <= BMI < 30):
        return "<h1>You are overweight (Thừa cân)</h1>"
    else:
        return "<h1>You are obese (Béo phì)</h1>"




@app.route('/bai3demo')
def bai3():
    return render_template("bai3demo.html")


@app.route('/bai2demo')
def bai2():
    return render_template("bai2demo.html")


@app.route('/school')
def direct():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
  app.run( debug=True)
