from flask import Flask, render_template, request
from copy_of_untitled7 import predict_gamma
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    actual = None
    graph_url = None

    if request.method == 'POST':
        ZL = float(request.form['ZL'])
        Z0 = float(request.form['Z0'])

        prediction, actual = predict_gamma(ZL, Z0)

        # Create graph
        plt.figure()
        plt.scatter([actual], [prediction])
        plt.plot([-1,1], [-1,1])
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("Actual vs Predicted")

        # Save to memory
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        graph_url = base64.b64encode(img.getvalue()).decode()

        plt.close()

    return render_template('index.html',
                           prediction=prediction,
                           actual=actual,
                           graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug=True)