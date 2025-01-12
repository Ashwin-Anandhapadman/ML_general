from flask import Flask, render_template, request

app =Flask (__name__) #intializing the flask


@app.route("/") 
def welcome():
    return "<html><H1> Welcome to my webpage. I am ash </H1> </html>"


@app.route("/index") 
def idx_page():
    return render_template('index.html')


@app.route("/ash", methods= ['GET', 'POST'])
def ash_pg():
   if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
   return render_template('form.html')
    




'''
in the above route we use the jinga2  fucntion render_template that
helps us to link to other html pages. the index.html page should be created within
the "templates folder" in the same dir. as this python file. The function searches
for index.html within the templates folder
'''

#the flask intialization has an attribute from the __name__ function that is used in all python prpojects to define the major code block for exectuion
if __name__=="__main__": 
    app.run(debug=True)

