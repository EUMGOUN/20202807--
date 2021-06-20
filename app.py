from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/monster')
def monster():
    return render_template('monster.html')

@app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@app.route('/AdventurersNote')
def AdventurersNote():
    return render_template('AdventurersNote.html')

@app.route('/rest')
def rest():
    return render_template('rest.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/Happy')
def Happy():
    return render_template('Happy.html')

@app.route('/talk')
def talk():
    return render_template('talk.html')

@app.route('/talkmore')
def talkmore():
    return render_template('talkmore.html')

@app.route('/bad')
def bad():
    return render_template('bad.html')

@app.route('/Attack')
def Attack():
    return render_template('Attack.html')

@app.route('/Attacktrue')
def Attacktrue():
    return render_template('Attacktrue.html')

@app.route('/Forest')
def Forest():
    return render_template('Forest.html')



@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        return "POST로 전달"

#if __name__ == '__start__':
#    app.run(debug=True)