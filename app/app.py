from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "devops-demo-api",
        "message": "Hello from WSL Ubuntu!"
    })

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Pipeline Demo API",
        "endpoints": ["/health", "/"]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)