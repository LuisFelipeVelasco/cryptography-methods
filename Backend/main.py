from flask import Flask , jsonify,request
import atbash_cipher as atbash
import Cesar.cesar_cipher as Cesar
import Cesar.cesar_hack as CesarH
import Simple_Column_Transposition.simple_column_transposition_cipher as ScTransposition
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

@app.route("/cesar/encrypt", methods=["POST"])
def cesar_encrypt():
    data=request.get_json()
    key=data["key"]
    user_message=data["message"]
    message_encrypted=Cesar.encrypt(key,user_message)
    return jsonify({"result":message_encrypted}),200

@app.route("/cesar/decrypt", methods=["POST"])
def cesar_decrypt():
    data=request.get_json()
    key=data["key"]
    user_message=data["message"]
    message_desencrypted=Cesar.decrypt(key,user_message)
    return jsonify({"result":message_desencrypted})

@app.route("/cesar/break", methods=["POST"])
def cesar_break():
    data=request.get_json()
    user_message=data["message"]
    message_breaked=CesarH.cesar_break(user_message)
    return jsonify({"result":message_breaked})

@app.route("/transposition/encrypt/<key>/<user_message>/<Number_Of_Characteres_Joined>")
def simple_column_transposition_encrypt(key,user_message,Number_Of_Characteres_Joined):
    message_encrypted=ScTransposition.Encrypt(key,user_message,Number_Of_Characteres_Joined)
    return jsonify({"result":message_encrypted})

@app.route("/transposition/decrypt/<key>/<user_message>")
def simple_column_transposition_decrypt(key,user_message):
    message_desencrypted=ScTransposition.Encrypt(key,user_message)
    return jsonify({"result":message_desencrypted})

@app.route("/transposition/break/<user_message>")
def simple_column_transposition_break(user_message):
    message_breaked=ScTransposition.Encrypt(user_message)
    return jsonify({"result":message_breaked})

if __name__=="__main__":
    app.run(debug=True)