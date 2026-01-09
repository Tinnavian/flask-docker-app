from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello from Docker container!"
	return "OMG is this v1.01 update???"

@app.route('/health')
def health():
	return {"status": "healthy", "service": "flask-app"}, 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
