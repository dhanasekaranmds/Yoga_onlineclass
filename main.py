from flask import Flask, flash, request, session, Response, url_for, send_from_directory, current_app, \
    send_file, render_template
import pymysql
app=Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY']='7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/classes")
def classes():
    return render_template('classes.html')

@app.route("/registration")
def registration():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/user_registration",methods=['GET','POST'])
def user_registration():
    if request.method=='POST':
        name=request.form['name']
        dob=request.form['dob']
        currentage=request.form['currentage']
        contact=request.form['contact']
        address=request.form['address']
        city=request.form['city']
        pincode=request.form['pincode']

        conn=pymysql.connect(user='root',password='',host='localhost', database='cbe',charset='utf8')
        cursor=conn.cursor()
        cursor.execute("insert into yoga_site values('"+name+"','"+dob+"','"+currentage+"','"+contact+"','"+address+"','"+city+"','"+pincode+"')")
        conn.commit()
        cursor.close()
        return render_template('register.html')

@app.route("/user_login",methods=['GET','POST'])
def user_login():
    msg=None
    if request.method=='POST':
        n = request.form['name']
        g = request.form['dob']
        n1 = str(n)
        g1 = str(g)
        q = ("SELECT * from yoga_site where name='" + str(n1) + "' and dob='" + str(g) + "'")
        conn = pymysql.connect(user='root', password='', host='localhost', database='cbe', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        check = len(data)
        if check == 0:
            return render_template("login.html")
        else:
            return render_template(("login.html"))

if __name__=='__main__':
    app.run(debug=True,use_reloader=True,host="0.0.0.0")