from biudzetas import Biudzetas
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

biudzetas = Biudzetas()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/zurnalas/")
def zurnalas():
    zurnalas = biudzetas.zurnalas
    return render_template("zurnalas.html", zurnalas=zurnalas)


@app.route("/balansas/")
def balansas():
    balansas = biudzetas.gauti_balansa()
    return render_template("balansas.html", balansas=balansas)


@app.route("/ivestipajamas/", methods=['GET', 'POST'])
def ivestipajamas():
    if request.method == "GET":
        return render_template('pajamu_forma.html')
    if request.method == "POST":
        suma = float(request.form['suma'])
        siuntejas = request.form['siuntejas']
        info = request.form['info']
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
        return redirect('/zurnalas/')


@app.route("/ivestiislaidas/", methods=['GET', 'POST'])
def ivestiislaidas():
    if request.method == "GET":
        return render_template('islaidu_forma.html')
    if request.method == "POST":
        suma = float(request.form['suma'])
        atsiskaitymo_budas = request.form['atsiskaitymo_budas']
        isigyta_preke_paslauga = request.form['isigyta_preke_paslauga']
        info = request.form['info']
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
        return redirect('/zurnalas/')


if __name__ == "__main__":
    app.run(debug=True)
