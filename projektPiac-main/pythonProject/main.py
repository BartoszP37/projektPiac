from flask import Flask, render_template, request,abort, redirect, url_for, make_response
from flask_mail import Mail, Message
from flask_dance.contrib.github import make_github_blueprint, github
from flask_restful import Resource, Api
import secrets 
import os
import time
#from AzureDB import AzureDB

app = Flask(__name__)
api=Api(app)
mail= Mail(app)

app.secret_key=secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT']='1'

github_blueprint=make_github_blueprint(
    client_id="e2e5a303054d19d8893c",
    client_secret="05c67984f54eedfead7b821b0b2972b5d87d1064",
)

app.register_blueprint(github_blueprint, url_prefix='/login')

class Quotes(Resource):
    def get(self):
        quotes = {
            'Elon Musk': {
                'quote': 'Fajnie byłoby umrzeć na Marsie, byle nie rozbić się przy podejściu do lądowania.'
            },
            'Steve Balmer': {
                'quote': 'Mam Maka i czas pracy na bateriach jest fatalny, Mac jest taaaki ciężki. Jeśli chcesz długo pracować na komputerze – lepiej zrobić przesiadkę. Jeśli chcesz netbooka – lepiej zrobić przesiadkę. Jeśli chcesz korzystać z tych samych aplikacji, które ma Mac plus wielu innych – lepiej zrobić przesiadkę. MacBook Air jest lekki? Podnieście te komputery, które mamy tutaj, są dużo lżejsze!'
            },
            'Steve Jobs': {
                'quote': 'Ci, którzy są wystarczająco szaleni, by myśleć, że są w stanie zmienić świat, są tymi, którzy go zmieniają'
            },
            'Bill Gates': {
                'quote': 'Obecnie ludzie od bezpieczeństwa włamują się do maców każdego dnia, wymyślają nowe exploity, dzięki którym można całkowicie przejąć kontrolę nad maszyną. Niech ktoś spróbuje coś takiego zrobić z Windowsem chociaż raz na miesiąc.'
            },
            'Bill Gates': {
                'quote': 'Sprawdzanie postępów programisty za pomocą liczby linii kodu, które napisał, jest jak sprawdzanie postępów w budowaniu samolotu poprzez przyrost jego wagi'
            },
            'Fred Brooks':{
                'quote': 'To, co jeden programista może zrobić w miesiąc, dwóch programistów zrobi w dwa miesiące.'
            }
        }
        return quotes

    def put(self):
        author = request.form.get('author')
        quote = request.form.get('quote')

        if author and quote:
            self.quotes[author] = {'quote': quote}
            return {author: self.quotes[author]}
        else:
            return {'error': 'Pole autor i cytat nie mogą być puste.'}, 400

    def post(self):
        author = request.form.get('author')
        quote = request.form.get('quote')

        if author in self.quotes:
            self.quotes[author]['quote'] = quote
            return {author: self.quotes[author]}
        else:
            return {'error': f'Autor "{author}" nie istnieje.'}, 404

    def delete(self):
        author = request.form.get('author')

        if author in self.quotes:
            del self.quotes[author]
            return {'message': f'Cytat autora: {author} został usunięty.'}
        else:
            return {'error': f'Autor "{author}" nie istnieje.'}, 404
        
        
api.add_resource(Quotes, '/cytaty')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] =''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail")
def mail():
    msg = Message('Hello', sender ='yourId@gmail.com',recipients =['someone1@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

@app.route('/login')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info=github.get('/user')
        if account_info.ok:
            account_info_json=account_info.json()
            return redirect(url_for('index'))
        return '<h1> Request failed!</h1>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return app.send_static_file('aboutme.html')

@app.route('/gallery')
def gallery():
    return app.send_static_file('gallery.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/ksiega')
def ksiega():
    return app.send_static_file('ksiegagosci.html')

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#@app.route('/baza')
#def baza():
   # with AzureDB() as a:
        #data=a.azureGetData()
    #return render_template("result.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
