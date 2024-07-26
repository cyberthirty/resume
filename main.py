from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping')
def ping():
    target = request.args.get('target')
    result = subprocess.run(['ping', '-c', '4', target], capture_output=True, text=True)
    return result.stdout

@app.route('/nmap')
def nmap():
    target = request.args.get('target')
    result = subprocess.run(['nmap', target], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
