from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/somar')
def route_somar():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(resultado=somar(a, b))

@app.route('/subtrair')
def route_subtrair():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(resultado=subtrair(a, b))

@app.route('/multiplicar')
def route_multiplicar():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(resultado=multiplicar(a, b))

@app.route('/dividir')
def route_dividir():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = dividir(a, b)
    return jsonify(resultado=resultado)

@app.route('/calcular')
def calcular():
    expr = request.args.get('expr', '')
    try:
        # Segurança básica: só permite números e operadores
        if not all(c in "0123456789+-*/.()" for c in expr):
            raise ValueError("Expressão inválida")
        result = eval(expr)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': 'Erro'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


