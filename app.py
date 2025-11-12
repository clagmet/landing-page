from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(debug=True)

# создает небольшой веб сервак.
# не забыть написать в консоли pip install flask