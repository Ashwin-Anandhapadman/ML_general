#build dynamic URL and jinja2 template engine
#variable rule

## Jinja2 template engine
'''
below are formats for html files in jinja2 template engine

{{}}: expressions to print output in html (check result.html)
{%... %}: for conditional statements and loops 
{#... #}: for comments

'''


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
    
#VARIBLE RULES
# below the parameter score is restricted to a particular data type (int)...this is variable rule
'''
#@app.route('/success/<int:score>') #SCORE is a paramter
def success(score):
    return f'The score is {score}'
'''

#build dynamic URL
@app.route('/dysuccess/<score>') #SCORE is a paramter
def success(score):
    score = int(score)
    res=''
    if score>=50:
        res='pass'
    else:
        res='fail'
    return render_template('result.html', results=res)

#we created a html page to displat the results. A paramter results is made to store the res scores obtained from function
'''
WHY MAKE int(score)???
becuz we pass the scores as an URL (we type dysuccess/89)...so URL numbers can be
compared with operators like >= given inside function becuz they r seen as string
'''


#build dynamic URL - key-value pair format of jiinja2
@app.route('/ressuccess/<score>') #SCORE is a paramter
def success1(score):
    score = int(score)
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'

    full_score= {'score':score, 'result':res}
    return render_template('result1.html', results=full_score)

'''
the above example is slighly different from previous one. 
HERE, instead of passing the result directly, we pass them as key-val pairs
so we need to have create conditional loops inside result1.html to display the results
'''



#the flask intialization has an attribute from the __name__ function that is used in all python prpojects to define the major code block for exectuion
if __name__=="__main__": 
    app.run(debug=True)

