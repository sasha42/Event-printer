from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/badge/', defaults={'name':'test','skills':'Dev'})
@app.route('/badge/<name>/<skills>/')
def badge(name, skills):
	return render_template('badge.html', name=name, skills=skills)

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host='0.0.0.0')