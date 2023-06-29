from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello_World():
	return "hello world"

@app.route('/name')
def namefunc():
	return "Lee Dong-Hun"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="9000")
