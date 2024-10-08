from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    gas = data.get('gas')
    flame = data.get('flame')
    light = data.get('light')

    # Logic to generate a prediction can be added here
    prediction = "Normal" if gas < 300 and flame < 50 and light > 500 else "Alert"

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
