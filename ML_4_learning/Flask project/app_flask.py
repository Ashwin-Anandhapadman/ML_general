from flask import Flask

app =Flask (__name__) #intializing the flask
'''
creates an instance of flask class...which will be our WSGI application
'''

@app.route("/") #defining the route for displaying the message in webpage..here the route is home page ("/")
def welcome():
    return "welcome to this flask project. this is my proj. I am ash"

'''
once we intialize the flask class with "app" variable, we can then define the route for
accessing the webpage. "/" indicates the first page/main page or home page.
the IP address of the local host followed by /, gives us this route mentioned above
we get too see a webpage with the msg displayed above when this flask is run
Default port is 5000
'''

#we can create any number of routes as we need...below is index route

@app.route("/index") 
def idx_page():
    return "welcome to this index page"

#the flask intialization has an attribute from the __name__ function that is used in all python prpojects to define the major code block for exectuion
if __name__=="__main__": #this is going to be entry point of ".py" file and exceution starts here
    app.run(debug=True)

'''
debug=True helps us update the changes to the return statement above in realtime on
the webpage. Once we make the changes in the msg above and save the python file,
we can see the server reloads again and updates the changes by itself

'''