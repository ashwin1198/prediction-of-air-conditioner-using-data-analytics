from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def student():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      predict = request.form
      val=predict
      name=val['uname']
      pas=val['psw']
      print(name,pas)
      if(name=='ashwin' and pas=='1234'):
            return render_template("mini.html", result=predict)
      else:
          return render_template("login.html",result=predict)
@app.route('/form.html')
def form():
   return render_template("form.html")
@app.route('/mini.html')
def mini():
   return render_template("mini.html")
@app.route('/survey.html')
def survey():
   return render_template("survey.html")
@app.route('/sur',methods = ['POST', 'GET'])
def sur():
   return render_template("surveyres.html")
@app.route('/pre',methods = ['POST', 'GET'])
def pre():
   if request.method == 'POST':
      predict = request.form
      val=predict
      print(val,type(val))
      from sklearn.externals import joblib
      acm=joblib.load('ac.pkl')
      drym=joblib.load('dry.pkl')
      washm=joblib.load('wash.pkl')
      print(val['kwh'])
      a=val['kwh']
      a=int(a)
      b=val['money']
      b=int(b)
      d=val['people']
      ac=acm.predict([[a,b,d,a*3.142]])
      dry=drym.predict([[a,b,d,a*3.142]])
      wash=washm.predict([[a,b,d,a*3.142]])
      e=[ac,dry,wash]
      print(e)
      print(ac,dry,wash)
      return render_template("res.html", result=predict,variable=e)


if __name__ == '__main__':
   app.run(port=2500, debug = True)

