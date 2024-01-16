
from flask import Flask,render_template,request,session,url_for,redirect,flash
import sqlite3
app=Flask(__name__)
app.secret_key="123"
@app.route('/')
def form():
    return render_template('form.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        con=sqlite3.connect("data1.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from signup where email=? and phone=?",(email,password))
        data=cur.fetchone()
        if data:
            return redirect('home')
            
        else:
            flash("Error login page","danger")
    return render_template('form.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        try:
            name=request.form['uname']
            email=request.form['email']
            date=request.form['date']
            phone=request.form['phone']
            gender=request.form['gender']
            con=sqlite3.connect("data1.db")
            con.execute("create table if not exists signup (pid integer primary key,name text,email text,date date,phone int ,gender text)")
            cur =con.cursor()
            cur.execute("insert into signup (name,email,date,phone,gender)values(?,?,?,?,?)",(name,email,date,phone,gender))
            con.commit()
            flash("Record Added successfully","success")


        except:
            flash("Record Added Error","danger")

        finally:
            return redirect(url_for('form'))
            con.close()
    return render_template("signup.html")

@app.route('/about')
def about(): 
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/view')
def view():
    con=sqlite3.connect('data1.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select  * from job")
    data=cur.fetchall()
    con.close()
    return render_template('view.html',data=data)

@app.route("/register",methods=['GET','POST'])
def register():
    
    if request.method=='POST':
        try:
           
            fname=request.form['fname']
            pos=request.form['pos']
            address=request.form['address']
            dob=request.form['dob']
            edu=request.form['edu']
            inst=request.form['inst']
            grade=request.form['grade']
            work=request.form['work']
            con=sqlite3.connect("data1.db")
            con.execute("create table if not exists job (pid integer primary key,fname text,pos text,address text,dob date,edu text,inst text,Grade text,work text )")
            cur =con.cursor()
            cur.execute("insert into job (fname,pos,address,dob,edu,inst,Grade,work)values(?,?,?,?,?,?,?,?)",(fname,pos,address,dob,edu,inst,grade,work))
            con.commit()
            flash("Record Added successfully","success")


        except:
            flash("Record Added Error","danger")

        finally:
            return redirect(url_for('home'))
            con.close()
    return render_template("register.html")

if __name__=='__main__':
    app.run(debug=True)