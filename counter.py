
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def count():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('counter.html', counter=session['counter'])


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/count')
def count_session():
    session['counter'] += 2
    return render_template('counter.html', counter=session['counter'])


@app.route('/add_count', methods=['post'])
def addcount():
    count = request.form['count']
    session['counter'] += int(count)
    return render_template('counter.html', counter=session['counter'])


if __name__ == "__main__":
    app.run(debug=True, port=5006)
