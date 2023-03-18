from flask import Flask, render_template, redirect
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

data = pd.read_csv("data.csv")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/facecream')
def facecream():
    plt.bar(data['month_number'], data['facecream'])
    plt.ylabel("Units Sold")
    plt.xlabel("Months")
    plt.savefig("static/facecream.png")
    plt.close()
    return redirect('/face_page')


@app.route('/face_page')
def face_page():
    return render_template("face_page.html")


@app.route('/facewash')
def face_wash():
    plt.bar(data['month_number'], data['facewash'])
    plt.ylabel("Units Sold")
    plt.xlabel("Months")
    plt.savefig("static/facewash.png")
    plt.close()
    return render_template("facewash.html")


@app.route('/toothpaste')
def toothpaste():
    plt.bar(data['month_number'], data['toothpaste'])
    plt.ylabel("Units Sold")
    plt.xlabel("Months")
    plt.savefig("static/toothpaste.png")
    plt.close()
    return render_template("toothpaste.html")


@app.route('/bathingsoap')
def bathingsoap():
    plt.bar(data['month_number'], data['bathingsoap'])
    plt.ylabel("Units Sold")
    plt.xlabel("Months")
    plt.savefig("static/bathingsoap.png")
    plt.close()
    return render_template("bathingsoap.html")


@app.route('/shampoo')
def shampoo():
    plt.bar(data['month_number'], data['shampoo'])
    plt.ylabel("Units Sold")
    plt.xlabel("Months")
    plt.savefig("static/shampoo.png")
    plt.close()
    return render_template("shampoo.html")


@app.route('/moisturizer')
def moisturizer():
    plt.bar(data['month_number'], data['moisturizer'])
    plt.ylabel("Units Sold")
    plt.xlabel("Months")
    plt.savefig("static/moisturizer.png")
    plt.close()
    return render_template("moisturizer.html")


if __name__ == '__main__':
    app.run()
