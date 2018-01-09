from flask import Flask, request
import requests
import json
import re

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Task 2
# Write a return statement such that it displays 'Welcome to <course_name>'
# when you navigate to localhost:5000/course/<course_name>
# Remember to get rid of the pass statement
@app.route('/course/<course>')
def course(course):
   return '<h1>Welcome to {}'.format(course)

# Task 3.1
# Edit the HTML form such that form data is sent to localhost:5000/result using POST method
@app.route('/form')
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="/result" method="POST"> 
  INGREDIENT:<br>
  <input type="text" name="ingredient" value="eggs">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
# Note that by default eggs would be entered in the input field
    return s


## Task 3.2
## Modify the function code and return statement
## to display recipes for the ingredient entered
@app.route('/result',methods = ['POST', 'GET']) # sending data using the POST method from /form
def displayData():
    if request.method == 'POST':

      search_term = request.form['ingredient'] ## ACCESSING DATA FROM /form

      base_url = "http://www.recipepuppy.com/api/"
      params_dict = {'i':search_term}
      response = requests.get(base_url, params=params_dict)

      recipes_dict = json.loads(response.text)
      return_str = "<p>"
      for recipe in recipes_dict['results']:
        return_str = return_str + recipe['title'] +'\n\n\n'
      return_str = return_str + '</p>'

      return return_str

## Task 4
## Note : Since this is a dyanmic URL, recipes function should recieve a paramter called `ingrdient` 
@app.route('/recipe/<ingredient>')
def recipes():
    pass

if __name__ == '__main__':
    app.run()
