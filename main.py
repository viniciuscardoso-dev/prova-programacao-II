from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    numero_aleatorio = ''
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        numero_aleatorio = random.randint(num1, num2)
    return render_template('index.html', numero_aleatorio=numero_aleatorio)

if __name__ == '__main__':
    print("Servidor Flask rodando em http://localhost:5000")
    app.run(debug=True)
