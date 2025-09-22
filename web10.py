from flask import Flask, render_template

app = Flask ("__name__")

@app.route("/")
def home():
    data = [
        {
            'nama' : 'adventa',
            'email': 'lala@gmail.com',
            'alamat' : 'sleman'
        },
        {
            'nama' : 'dyah',
            'email': 'dyaha@gmail.com',
            'alamat' : 'sleman'
        },
        {
            'nama' : 'puti',
            'email': 'puti@gmail.com',
            'alamat' : 'sleman'
        }
    ]
    return render_template('user.html', users = data)

if __name__ == '__main__':
    app.run(debug=True)