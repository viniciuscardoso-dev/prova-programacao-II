# Aplicação Flask de Número Aleatório

Esta é uma aplicação Flask simples que gera um número aleatório com base em dois números fornecidos pelo usuário.

## Pré-requisitos

Antes de começar, você precisará ter o Python instalado em sua máquina. Esta aplicação foi testada com o Python 3.8.

## Configuração do Ambiente Virtual

Para criar um ambiente virtual no Linux, siga estes passos:

1. Navegue até o diretório do projeto no terminal.
2. Execute o comando para criar um ambiente virtual:
   ```
   python3 -m venv venv
   ```
3. Ative o ambiente virtual:
   ```
   source venv/bin/activate
   ```

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

```
pip install flask
```

## Executando a Aplicação

Para iniciar a aplicação no Linux, execute:

```
export FLASK_APP=app.py
flask run
```

Ou, se preferir, você pode usar o comando `python` diretamente:

```
python app.py
```

A aplicação estará acessível em `http://localhost:5000`.

## Uso da Aplicação

1. Abra o navegador e vá para `http://localhost:5000`.
2. Você verá um formulário onde poderá inserir dois números.
3. Após inserir os números, clique no botão para gerar um número aleatório.
4. O número aleatório será exibido na tela.

## Desativação do Ambiente Virtual

Quando terminar de usar a aplicação no Linux, você pode desativar o ambiente virtual com:

```
deactivate
```