from flask import Flask , jsonify
import atbash_cipher as atbash
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hola"

@app.route("/atbash/<message>")
def atbash_cipher(message):
    message=atbash.codify(message)
    return jsonify({"result":message}),200

if __name__=="__main__":
    app.run(debug=True)