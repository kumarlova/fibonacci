# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

from flask import Flask, render_template, request

app = Flask(__name__)

def fibonacci(n):
    if n < 0:
        return "incorrect input"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fibonacci', methods=['POST'])
def calculate_fibonacci():
    try:
        n = int(request.form['number'])
        fib_seq = fibonacci(n)
        return render_template('result.html', number=n, sequence=fib_seq)
    except ValueError:
        return render_template('index.html', error="Please enter a valid positive integer.")

if __name__ == '__main__':
    app.run(debug=True)

