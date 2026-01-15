from flask import Flask , jsonify
import atbash_cipher as atbash
import Cesar.cesar_cipher as Cesar
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hola"

@app.route("/atbash/<user_message>")
def atbash_cipher(user_message):
    message=atbash.codify(user_message)
    return jsonify({"result":message}),200

@app.route("/cesar_encrypt/<key>/<user_message>")
def cesar_encrypt(key,user_message):
    message=Cesar.encrypt(key,user_message)
    return jsonify({"result":message}),200

@app.route("/cesar_decrypt/<key>/<user_message>")
def cesar_decrypt(key,user_message):
    message=Cesar.decrypt(key,user_message)
    return jsonify({"result":message})

if __name__=="__main__":
    app.run(debug=True)