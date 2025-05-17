from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open('personality_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    lemmatizer = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form["user_input"]
    processed = vectorizer.transform([user_input])
    prediction = model.predict(processed)
    predicted_label = encoder.inverse_transform([prediction[0]])[0]
    return render_template("index.html", prediction=predicted_label)


if __name__ == '__main__':
    app.run(debug=True)
