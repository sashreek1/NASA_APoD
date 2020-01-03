from app import app
from flask import request, render_template
import requests
from get_pdf import get_pdf
from flask import send_file

date = None

def get_img(date):
    url = 'https://api.nasa.gov/planetary/apod?api_key=pIcRQCA2adaaBmYNlCeY2vltnWKuptYoayhIDbYc&date='+date
    r = requests.get(url)
    r = r.json()
    try:
        return r['hdurl'],r['explanation']
    except KeyError :
        return 'error','error'

@app.route('/')
@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    img,text = get_img(text)
    if img == 'error':
        return render_template('error_file.html')
    else:
        get_pdf(img,text)
        return render_template('home.html', title='Home', image=img)

@app.route('/downloads')
def show_static_pdf():
    return send_file('out.pdf', as_attachment=True, cache_timeout=5)