from flask import Flask, render_template, request, redirect
from views import shorten_url, redirect_to_long_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = shorten_url(long_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = redirect_to_long_url(short_url)
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
