# 🧠 Personality Prediction using Machine Learning (MBTI)

This project is a text-based personality prediction system built using Natural Language Processing (NLP) and Machine Learning. It predicts a user's Myers-Briggs Type Indicator (MBTI) personality type from their written text.

## 💡 Features

- Predicts one of 16 MBTI personality types (e.g., INTJ, ENFP, ISTP).
- Trained with a machine learning model using user-written text as input.
- Includes lemmatization, vectorization, and encoding steps.
- Flask-based web app for user interaction and prediction.
- Supports deployment on local machines or cloud platforms.

--

## 🗃️ Project Structure

├── app.py # Flask app backend
├── personality_prediction.ipynb # Model training and analysis
├── personality_prediction_model.pkl # Trained ML model
├── encoder.pkl # Label encoder
├── vectorizer.pkl # TF-IDF Vectorizer
├── lemmatizer.pkl # Lemmatizer object
├── static/ # Static files (CSS/JS)
├── templates/ # HTML templates
├── deployment images/ # Reference images (MBTI chart, etc.)

--

## 🧪 Tech Stack

- Python
- Scikit-learn
- NLTK
- Flask
- HTML

--

## 🔄 How It Works

1. User enters a text sample.
2. The system preprocesses the text (lemmatization, vectorization).
3. The trained model predicts the MBTI type (e.g., INFP, ESTJ).
4. The result is displayed along with a short personality description.
   ![deployment_img1](https://github.com/user-attachments/assets/c6d8cec0-abee-4f55-9348-0b219224a2f4)
   ![deployment_img2](https://github.com/user-attachments/assets/829a2c00-9935-4a5f-b9b8-05c94eacc3e2)
   ![deployment_img3](https://github.com/user-attachments/assets/2be33140-9233-4c4b-a19c-cad34b1e5a99)


--


## 📊 Myers-Briggs Personality Types
The system uses the MBTI framework, classifying individuals based on:

Extraversion (E) / Introversion (I)

Sensing (S) / Intuition (N)

Thinking (T) / Feeling (F)

Judging (J) / Perceiving (P)

![MyersBriggs_personality_Types](https://github.com/user-attachments/assets/8e8592ac-a951-48d3-a273-c96ff0fb2a6e)



## 📄 License
This project is for educational purposes.
