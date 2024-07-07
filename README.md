# NLP Website

This Flask application integrates with MongoDB for user data storage and utilizes various APIs for natural language processing tasks such as sentiment analysis, named entity recognition (NER), and emotion detection. Tailwind CSS is used for styling the frontend.

## Features

- **User Authentication**: Secure user registration and login system.
- **Text analysis functionalities**: Provides easy navigation to three main NLP functionalities:
  - Sentiment Analysis
  - Named Entity Recognition (NER)
  - Emotion Detection
- **Database Integration**: Uses MongoDB for data storage of users.

## Prerequisites

- Before running the application locally or deploying it, ensure you have the following installed and set up:
- **Python (3.7 or higher)**
- **MongoDB Atlas account (or local MongoDB instance)**
- **EdenAI API key (obtainable from [EdenAI]((https://docs.edenai.co/reference)))**

## Installation

 **Clone the repository**:
    
    git clone https://github.com/Panchalparth471/NLP-Website.git
    cd NLP-Website

 **Install the dependencies**:
   pip install -r requirements.txt

    
## Configuration
 # MongoDB URI for database connection
MONGODB_URL=mongodb+srv://your-username:your-password@cluster0.ko0ihta.mongodb.net/NLP

 # Eden AI API key for accessing natural language processing APIs
EDENAI_API_KEY=your-edenai-api-key

Make sure to replace MONGODB_URL and EDENAI_API_KEY with your actual MongoDB connection URI and Eden AI API key.

## Usage

0. **Get your api key from Eden AI**
   ``` From myapi.py file in the headers replace <YOUR_API_KEY/API_TOKEN> to the api key you got ```

1. **Run the Flask application**:
  ```
   python app.py
   ```
2. **User Registration/Login**:
- Create a new account or login with existing credentials.

3. **Select NLP Functionality**:
- Choose from Sentiment Analysis, Named Entity Recognition, or Emotion Detection.

4. **View Results**:
- Results from the selected NLP operation will be displayed in the interface.

## API Endpoints

```
/ - Homepage
/register - User registration page
/add_data - Endpoint to add user data to MongoDB
/login - User login endpoint
/home - User home page
/sentiment - Sentiment analysis page
/ner - Named entity recognition page
/emotion - Emotion detection page
/do_sentiment - Endpoint for performing sentiment analysis
/do_ner - Endpoint for performing named entity recognition
/do_emotion - Endpoint for performing emotion detection

```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your suggested changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## References

### Eden AI
Refer to the [Eden AI Documentation ](https://docs.edenai.co/reference).


### Flask

Flask is a lightweight WSGI web application framework in Python. It provides tools, libraries, and technologies that allow you to build web applications quickly and efficiently. For more information and documentation, visit the [Flask Official Website](https://flask.palletsprojects.com/).

### PyMongo

PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. For more information and documentation, visit the [PyMongo Official Website](https://pymongo.readthedocs.io/en/stable/).

### Tailwind CSS

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all the building blocks you need to build designs without any annoying opinionated styles you have to fight to override. For more information and documentation, visit the [Tailwind CSS Official Website](https://tailwindcss.com/).

### Tailwind CSS Resources

- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Tailwind CSS GitHub Repository](https://github.com/tailwindlabs/tailwindcss)



