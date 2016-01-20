from flask import Flask, render_template, request
import pyexcel as pe
import subprocess
from PIL import Image

app = Flask(__name__)
sheet = pe.get_sheet(file_name="orders.csv", name_rows_by_column=0)

def serial_print(orderid):
	return orderird

def fetch_order(orderid):
	id = orderid[:9]
	order = sheet.row[id]
	return(id, order)

@app.route('/')
def home():
  return render_template('layout.html')

@app.route('/badge/', defaults={'name':'test','skills':'Dev'})
@app.route('/badge/<name>/<skills>/')
def badge(name, skills):
	return render_template('badge.html', name=name, skills=skills)

@app.route('/scan', methods=['GET', 'POST'])
def scan():
	if request.method == 'POST':
		order = fetch_order(request.form['id'])
		subprocess.call(["/event-printer/phantomjs", "/event-printer/generate_badge.js", order[0]])
		badge = Image.open("/event-printer/badge.png")
		badge = badge.rotate(270)
		badge.save("/event-printer/badge2.png")
		subprocess.call(["/scripts/ql570/ql570", "/dev/usb/lp0", "w", "/event-printer/badge2.png"])
		return render_template('scanner.html', url=request.url_root)
	else:
		return render_template('scanner.html', url=request.url_root)

@app.route('/print')
def prtinty():
	orderid = request.args.get('id')
	sanitized_id = orderid[:9]
	order = sheet.row[sanitized_id]
	if order[4] == "Hackathon admission":
		order[4] = "Hackathon participant"
	return render_template('badge.html', name=order[0]+" "+order[1], skills=order[4])

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(debug=True, threaded=True, host='0.0.0.0')