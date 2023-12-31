from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def about_me():
    return render_template('wizytowka_1.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['comment']
        print('Received message:', message)
    return render_template('wizytowka_2.html')

if __name__ == '__main__':
    app.run()