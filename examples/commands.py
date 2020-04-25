from flask_slack import Flack, Dispatcher, request, jsonify

dp = Dispatcher()
app = Flack(__name__, dispatcher=dp)


@app.command
def hello():
    form = request.form['command']
    text = request.form['text']
    return jsonify({
        'text': f'You called `{form} {text}`'
    })


@app.command(name='abc')
def goodbye():
    return jsonify({
        'text': f'Mandril'
    })