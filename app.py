from flask import Flask, render_template

app = Flask(__name__)

@app.route('/capivaras')
def capivaras():

    nome="Capivaras"
    idade="Capivaras"
    animal="Capivaras"

    return render_template("index.html", nome=nome, idade=idade, animal=animal)

if __name__ == '__main__':
    app.run(debug=True)