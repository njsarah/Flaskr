from flask import Flask,request,session,g,redirect,url_for,\
    abort,render_template,flash
from connMySql import FlaskrDB
app = Flask(__name__)
app.config['dbconfig']={'host':'127.0.0.1',
        'user':'root',
        'password':'sdts12345678',
        'database':'flaskr',}
@app.route('/')
def show_entries():
    with FlaskrDB(app.config['dbconfig']) as cur:
        _SQL = '''select titel,text from entries order by id desc'''
        cur.execute(_SQL)
        entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
@app.route('/add', methods=['POST'])
def add_entry(req,res):
    #if not session.get('logged_in'):
        #abort(401)
    with FlaskrDB(app.config['dbconfig']) as cursor:
    	_SQL = '''insert into entries (titel, text) values(%s,%s)'''
    	cursor.execute(_SQL,(request.form['title'], request.form['text'],res,))
    #flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != "1234":
            error = 'Invalid username'
        elif request.form['password'] != "1234":
            error = 'Invalid password'
        else:
            #session['logged_in'] = True
            #flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
@app.route('/logout')
def logout():
    #session.pop('logged_in', None)
    #flash('You were logged out')
    return redirect(url_for('show_entries'))
if __name__ == '__main__':
	app.run(debug=True)