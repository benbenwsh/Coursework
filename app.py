from flask import Flask, render_template, request
from nlp.retrieval_model.chatbot import respond
print('finally')
app = Flask(__name__)       # Create application object as an instance of the Flask class
app.static_folder = 'static'

# The URL that the application implements
@app.route("/")     # When the browser requests the URL "/"
def home():     # View function (The code to execute when the client requests a given URL) for home page (chat screen)
    return render_template("index.html")        # HTML template for the home page

@app.route("/get")      # When the browser requests the URL "/get"
def get_bot_response():     # View function to get the response from the chatbot
    userText = request.args.get('msg')
    response = respond(userText)
    print(response)
    return response        # Returns the response generated by the model

if __name__ == "__main__":
    app.run()       # Runs the web application