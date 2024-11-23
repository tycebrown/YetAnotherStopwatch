from flask import Flask;
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/msg')
def getMsg():
    return 'It worked!'

if __name__ == '__main__': app.run();