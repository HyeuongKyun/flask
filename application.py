from flask import Flask, session, render_template, request, redirect, url_for
import sys
application = Flask(__name__)
application.secret_key = "lkjds#2-1@dsp!ldaskfj"
import database

ID = "hello"
PW = "world"

# @application.route("/home")
# def home():
#     if "userID" in session: #로그인이 된 상태
#         return render_template("home.html",username = session.get("userID"), login = True)
#     else:
#         return render_template("home.html",login=False)
    






@application.route("/")



def index():
    
    stylecss = f"/style.css"
    photo1 = f"img/maintitle.jpg"
    photo2 = f"img/search.png"
    photo3 = f"img/gym.jpg"
    photo4 = f"img/healthyfood.jpg"
    photo5 = f"img/equipment.jpg"
    photo6 = f"img/board.jpg"
    
    if "userID" in session: #로그인이 된 상태
        return render_template("index.html",username = session.get("userID"), login = True, photo1 = photo1, photo2 = photo2, photo3 = photo3,photo4 = photo4 , photo5 = photo5, photo6 = photo6,stylecss=stylecss)
    else:
        return render_template("index.html",login=False, photo1 = photo1, photo2 = photo2, photo3 = photo3,photo4 = photo4 , photo5 = photo5, photo6 = photo6,stylecss=stylecss)
    
    return render_template("index.html", photo1 = photo1, photo2 = photo2, photo3 = photo3,photo4 = photo4 , photo5 = photo5, photo6 = photo6,stylecss=stylecss)

# def home():
#     if "userID" in session: #로그인이 된 상태
#         return render_template("index.html",username = session.get("userID"), login = True)
#     else:
#         return render_template("index.html",login=False)
    




@application.route("/login", methods=["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")
    
    if ID == _id_ and _password_ == PW:
        #print(_id_,_password_)
        session["userID"] = _id_
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@application.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("index"))



# @application.route("/fitinfo")
# def fitinfo():
#     location = reguest.args.get("location")
#     cleaness = reguest.args.get("clean")
#     built_in = reguest.args.get("built")
    
#     database.save(location,cleaness,built_in)
#     photo = f"img/maintitle.jpg"
#     return render_template("fitinfo.html", photo = photo)

@application.route("/fitinfo")
def fitinfo():
    # location = reguest.args.get("location")
    # cleaness = reguest.args.get("clean")
    # built_in = reguest.args.get("built")
    
    # database.save(location,cleaness,built_in)
    
    frequencyi = database.load_list()
    length = len(frequencyi)
    
    
    
    photo = f"img/maintitle.jpg"
    return render_template("fitinfo.html", photo = photo, frequencyi=frequencyi, length=length)


@application.route("/habit")
def habit():
    habitt = database.load_list_habit()
    length = len(habitt)
    
    photo = f"img/maintitle.jpg"
    return render_template("habit.html", photo = photo, habitt=habitt, length=length)


# @application.route("/list")
# def list():
#     house_list = database.load_list()
#     length = len(house.list)
#     return render_template()

if __name__ == "__main__":
    application.run(host='0.0.0.0')
