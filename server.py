from flask import Flask, render_template, request, flash, redirect, session, jsonify
from jinja2 import StrictUndefined
from face import face

app = Flask(__name__)
app.secret_key = 'yliwmhd'
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/face.json")
def face_json():
    image_url = request.args.get('image_url')
    data = face(image_url)

    return jsonify(data)

if __name__ == "__main__":
    # connect_db(app)
    # db.create_all()
    
    app.run(host="0.0.0.0", debug=True)