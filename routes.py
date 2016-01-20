from flask import Flask, render_template, request
import pyexcel as pe
 
app = Flask(__name__)
sheet = pe.get_sheet(file_name="orders.csv", name_rows_by_column=0)
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/badge/', defaults={'name':'test','skills':'Dev'})
@app.route('/badge/<name>/<skills>/')
def badge(name, skills):
	return render_template('badge.html', name=name, skills=skills)

@app.route('/scan')
def scan():
	orderid = request.args.get('id')
	sanitized_id = orderid[:9]
	order = sheet.row[sanitized_id]
	if order[4] == "Hackathon admission":
		order[4] = "Hackathon participant"
	return render_template('badge.html', name=order[0]+" "+order[1], skills=order[4])

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host='0.0.0.0')