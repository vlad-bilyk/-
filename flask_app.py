from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map():
    return render_template('map.html', x=5)


if __name__ == '__main__':
    app.run()