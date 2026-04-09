from flask import Flask, render_template, request
from copy_of_untitled7 import predict_gamma
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    actual = None

    if request.method == 'POST':
        try:
            ZL = float(request.form['ZL'])
            Z0 = float(request.form['Z0'])

            prediction, actual = predict_gamma(ZL, Z0)

        except Exception as e:
            prediction = "Error"
            actual = str(e)

    return render_template(
        'index.html',
        prediction=prediction,
        actual=actual
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))