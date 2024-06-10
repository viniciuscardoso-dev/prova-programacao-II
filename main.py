# Importa as bibliotecas necessárias para o funcionamento da aplicação web.
from flask import Flask, request, render_template
import random

# Cria uma instância da aplicação Flask.
app = Flask(__name__)

# Define a rota principal '/' e aceita métodos GET e POST.
@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa a variável que armazenará o número aleatório como uma string vazia.
    numero_aleatorio = ''
    # Verifica se o método da requisição é POST.
    if request.method == 'POST':
        # Obtém os números do formulário e os converte para inteiros.
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        # Gera um número aleatório entre num1 e num2.
        numero_aleatorio = random.randint(num1, num2)
    # Renderiza o template 'index.html' passando o número aleatório gerado.
    return render_template('index.html', numero_aleatorio=numero_aleatorio)

# Verifica se o script é o principal sendo executado.
if __name__ == '__main__':
    # Imprime uma mensagem no console.
    print("Servidor Flask rodando em http://localhost:5000")
    # Executa a aplicação com o modo de depuração ativado.
    app.run(debug=True)
