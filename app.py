from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc




app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sign.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200), nullable=False)
    def __repr__(self) -> str:
        return f"{self.sno} - exit{self.name} - {self.email}"
    


@app.route("/", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
       
        
        name = request.form.get('name')
        email = request.form.get('email')
        
        sign = User(name = name, email = email)
        db.session.add(sign)
        db.session.commit()
        tableAll = User.query.all()
        return render_template("table.html", allTables= tableAll)
        
      
   
       
    return render_template('sign_up.html')
@app.route("/delete/")
@app.route("/delete/<int:sno>")
def delete(sno):
    sign = User.query.filter_by(sno=sno).first()
    db.session.delete(sign)
    db.session.commit()
    tableAll = User.query.all()
    return render_template("table.html", allTables= tableAll)


    
    

if __name__=="__main__":
    app.run(debug=True)
    




