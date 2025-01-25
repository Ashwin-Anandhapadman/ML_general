from flask import Flask, render_template, request

app =Flask (__name__) #intializing the flask


@app.route("/") 
def welcome():
    return "<html><H1> Welcome to my webpage. I am ash </H1> </html>"


@app.route("/index") 
def idx_page():
    return render_template('index.html')


'''
GET: Used to request data from a specified resource.
When you access a URL or click on a link, your browser sends a GET request to the server.
Parameters are sent in the URL (query string), making them visible in the address bar.

POST: Used to send data to a server to create/update a resource.
When you submit a form, the browser sends a POST request with the form data.
'''



@app.route('/form', methods= ['GET', 'POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template('form.html')

'''
When a user fills out this form and submits it, the 
POST request is sent to the server, where the form() 
function processes it and returns a personalized greeting
'''
#the flask intialization has an attribute from the __name__ function that is used in all python prpojects to define the major code block for exectuion
if __name__=="__main__": 
    app.run(debug=True)

