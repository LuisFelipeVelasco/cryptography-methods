from flask import Flask , jsonify
import atbash_cipher as atbash
app= Flask(__name__)

@app.route("/")
def home():
    return "Hola"

@app.route("/atbash/<message>")
def atbash_cipher(message):
    message=atbash.codify(message)
    return jsonify(message),200

if __name__=="__main__":
    app.run(debug=True)