import os;
from flask import Flask, render_template;
from flask_cors import CORS

app = Flask(__name__, static_url_path="", static_folder='/yet-another-stopwatch/dist')
CORS(app)

@app.route('/api/msg')
def getMsg():
    return 'It worked!'

if __name__ == '__main__': 
        app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)));