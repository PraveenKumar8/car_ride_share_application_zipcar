from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if request.form.get('query1') == 'Run Query1':
            # return render_template('query1.html')
            print("pressed button 1")
            return render_template('hello.html')
        elif request.form.get('query2') == 'Run Query2':
            # pass # do something 
            print("pressed button 2")
            return render_template('hello.html')
        elif request.form.get('query3') == 'Run Query3':
            # pass # do something
            print("pressed button 3")
            return render_template('hello.html')
        elif request.form.get('query4') == 'Run Query4':
            # pass # do something
            print("pressed button 4")
            return render_template('hello.html')
        else:
            print("nothing pressed")
            return render_template('hello.html')
    elif request.method == 'GET':
        return render_template('hello.html')