import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    message_options = ["This is Black!!!!",
                       "Its Black and Hell is Hot...",
                       "I'm Black...",
                       "I am BlackMan!!!!",
                       "I am BlackWoman!!!!"

                      ]

    message = """
    <!DOCTYPE html>
        <html>
            <body style="background-color:black;">

            <h1 style="color:white;">{}</h1>
           
        </body>
    </html>
    """.format(random.choice(message_options))

    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0')
