
from flask import Flask,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__,template_folder="templates")
app.secret_key="justkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/abdul/OneDrive/Masaüstü/Yeni klasör/başlıyoruz/orm yapısı için web sitesi/database.db"
db.init_app(app)
@app.route("/sorgu",methods=["POST"])
def sorgu():
    sorgu1=request.form.get("sorgu")
    sorgu2=request.form.get("soyad1")
    database1 = database.query.filter(database.title.like("%"+sorgu1+"%"), database.soyad.like("%"+sorgu2+"%")).all()
    db.session.commit()
    return render_template("sorgu.html",database1=database1)#altaki index fonksiyonun adına göre
# @app.route("/complete/<string:id>")
#"""def complete(id):
#    data=database.query.filter_by(id = id).first()
 #    data.soyad=not data.soyad
 #    db.session.commit()
#     return redirect(url_for("index1"))"""
@app.route("/delete/<string:id>")
def delete(id):
    data=database.query.filter_by(id = id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for("index1"))
@app.route("/add",methods=["POST"])
def add():
    title=request.form.get("title")
    soyad=request.form.get("soyad")
    tc=request.form.get("tc")
    yenidata=database(title=title,soyad=soyad,tc=tc)#alttaki complete ile aynı
    db.session.add(yenidata)
    db.session.commit()
    return redirect(url_for("index1"))#altaki index fonksiyonun adına göre
@app.route("/")
def index1():
    database1=database.query.all()
    return render_template("indexx1.html",database1=database1)
class database(db.Model):#burası zorunlu
    __tablename__ = 'mytable'
    id = db.Column(db.Integer, primary_key=True)
    #flask_sqlalchemy sayfasından aldık
    title=db.Column(db.String(80))
    soyad=db.Column(db.String(80))
    tc=db.Column(db.String(80))
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)