from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app=Flask(__name__)

led_pin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT, initial=False)

@app.route('/')
def main():
	return render_template('test.html')

@app.route('/get')
def get():
	return render_template('get.html')

@app.route('/post')
def post():
	return render_template('default.html')

@app.route('/led/on')
def led_on():
	try:
		GPIO.output(led_pin, True)
		return "ok"
	except KeyboardInterrupt:
		GPIO.cleanup()
		return "fail"

@app.route('/led/off')
def led_off():
	try:
		GPIO.output(led_pin, False)
		return "ok"
	except KeyboardInterrupt:
		GPIO.cleanup()
		return "fail"

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
