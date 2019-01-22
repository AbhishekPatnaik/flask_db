from flask import Flask, render_template, request



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("search.html")

@app.route("/login")
def load_login():
    return render_template("login.html")


@app.route('/login',methods=['POST'])
def get_login_info():
    firstName = request.form['username']
    lastName = request.form['password']
    print(firstName,lastName)
    return "ok done"





if __name__ == "__main__":
    app.run(debug=True)
