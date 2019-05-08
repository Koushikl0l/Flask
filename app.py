from flask import Flask,render_template,request
from  textblob import TextBlob
app=Flask(__name__)
@app.route('/send',methods=['GET','POST'])

def send():

	if request.method=='POST':
		comment=request.form['comment']
		word=TextBlob(u""+comment)
		z=word.translate(from_lang='bn',to='en')
		return render_template('new.html',comment=z)
		
	#comment=request.form['comment']
	return render_template('home.html')
	
if __name__=="__main__":
	app.run(debug=True)
	