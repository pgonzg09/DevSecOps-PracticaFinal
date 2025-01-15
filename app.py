"""
Web Flask para realizar operaciones aritméticas básicas entre dos números
para demostrar el funcionamiento de los diferentes Workflows implementados.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """
    Ruta principal
    """
    return "Hello, CI/CD with Docker!"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    """
    Suma dos números dados como parámetros en la URL.

    Args:
        num1: Primer número a sumar
        num2: Segundo número a sumar

    Returns:
        str: Una cadena con la operación y su resultado
    """
    return f"{num1} + {num2} = {num1 + num2}"


@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1, num2):
    """
    Resta dos números dados como parámetros en la URL.

    Args:
        num1: Número del que se resta (minuendo)
        num2: Número a restar (sustraendo)

    Returns:
        str: Una cadena con la operación y su resultado
    """
    return f"{num1} - {num2} = {num1 - num2}"


@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1, num2):
    """
    Multiplica dos números dados como parámetros en la URL.

    Args:
        num1: Primer número a multiplicar
        num2: Segundo número a multiplicar

    Returns:
        str: Una cadena con la operación y su resultado
    """
    return f"{num1} * {num2} = {num1 * num2}"


@app.route('/div/<int:num1>/<int:num2>')
def div(num1, num2):
    """
    Divide dos números dados como parámetros en la URL.

    Args:
        num1: Número a dividir (dividendo)
        num2: Número por el que se divide (divisor)

    Returns:
        str: Una cadena con la operación y su resultado, o un mensaje
            de error si se intenta dividir por cero
    """
    if num2 == 0:
        return "Error: Division by 0 not allowed."
    return f"{num1} / {num2} = {num1 / num2}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
