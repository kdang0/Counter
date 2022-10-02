from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "MAKE IT MAKE SENSE"

@app.route('/')
def index():
    if 'counter' in session and 'visit' in session:
        session['counter'] += 1   
        session['visit'] +=1
    elif 'visit' in session:
        session['visit'] +=1
        session['counter'] =1
    else:
        session['counter'] = 1
        session['visit'] = 1
        session['spec_counter'] = 1
    return render_template('index.html', counter = session['counter'], visit_counter = session['visit'], counter_incr = session['spec_counter'] )

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect("/")

@app.route('/plus_one')
def addOne():
    session['spec_counter'] = 1
    return redirect("/")

@app.route('/plus_two')
def addTwo():
    session['counter'] += 1
    session['spec_counter'] = 2
    return redirect("/")

@app.route('/reset_counter')
def reset_counter():
    session.pop('counter')
    return redirect('/')


@app.route('/specific_increment', methods = ['POST'])
def specify_increment():
    print(request.form)
    session['spec_counter'] = int(request.form['spec_counter'])
    session['counter'] += (session['spec_counter']-1)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

