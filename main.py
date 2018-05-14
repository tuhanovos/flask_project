from flask import Flask

app = Flask(__name__)


app.config.update(
    DEBUG=True,
    SECRET_KEY='key'
)

@app.route('/')
def home():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()
