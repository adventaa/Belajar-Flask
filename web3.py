from flask import Flask

app = Flask (__name__)

@app.route('/profile/<username>/<kerja>')
def profile(username,kerja):
    return "<h1>Halaman profile {} sebagai {}</h1>".format(username,kerja)

if __name__ == '__main__':
    app.run(debug=True)