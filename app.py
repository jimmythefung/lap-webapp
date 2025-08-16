from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            grams = float(request.form['grams'])
            price_per_gram = float(request.form['price_per_gram'])
            result = grams * price_per_gram
        except (ValueError, KeyError):
            result = 'Invalid input.'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
