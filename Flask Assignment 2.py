#!/usr/bin/env python
# coding: utf-8

# ## Flask Assignment 2 

# #### Q1. Explain GET and POST methods.

# The GET method is primarily used to retrieve data from a server. When a GET request is made, the server returns the requested data in the response. The data is sent in the URL query string as key-value pairs, which can be seen in the address bar of the browser. GET requests are typically used for retrieving information such as web pages, images, or other resources.
# 
# On the other hand, the POST method is primarily used to submit data to a server. When a POST request is made, the data is sent in the request body, rather than in the URL. This is useful when submitting sensitive information, such as passwords or credit card numbers, as it is not visible in the URL. POST requests are typically used for submitting information, such as when filling out a form or uploading a file to a server.

# #### Q2. Why is request used in Flask?

# Request is an object in the Flask web framework that represents an incoming HTTP request from a client to the server. It provides access to the data submitted in the request, such as form data, query parameters, and request headers.
# 
# Request is an important feature of Flask because it enables the application to handle user input and respond accordingly. For example, if a user submits a form on a web page, Flask can use the Request object to retrieve the form data and process it accordingly.
# 
# The Request object also provides access to other important information, such as the URL of the request, the HTTP method used (GET, POST, etc.), and the user agent string of the client making the request.
# 
# Overall, the Request object in Flask is a crucial component of building web applications, as it enables developers to handle user input and respond appropriately, based on the data submitted in the request.

# #### Q3. Why is redirect() used in Flask?

# The redirect() function is a built-in function in the Flask web framework that is used to redirect the user's browser to a different URL. It is commonly used in web applications to redirect the user to a different page or route after a form submission or some other action.
# 
# There are several reasons why redirect() is used in Flask:
# 
# Redirecting after form submissions: When a user submits a form on a web page, the form data is typically processed by the server, and then the user is redirected to a different page or route. This can be achieved using the redirect() function, which sends a redirect response to the browser, causing it to navigate to the specified URL.
# 
# Handling authentication and authorization: In some cases, a web application may require the user to authenticate or authorize before accessing certain resources. If the user is not authenticated or authorized, the redirect() function can be used to redirect them to a login page or an error page.
# 
# Handling errors and exceptions: If an error or exception occurs in a Flask application, the redirect() function can be used to redirect the user to an error page, where they can be informed of the error and provided with instructions on how to proceed.
# 
# Overall, the redirect() function is a useful feature in Flask that allows developers to redirect the user's browser to a different URL, based on various conditions and actions within the web application.

# #### Q4. What are templates in Flask? Why is the render_template() function used?

# In Flask, templates are used to render dynamic content to the user in response to a request. A template is a file that contains HTML, along with placeholders for dynamic content, which are filled in by the Flask application at runtime.
# 
# Templates are an important feature of Flask, as they enable developers to create dynamic web pages that can display different content based on user input, data from a database, or other factors.
# 
# The render_template() function is a built-in function in Flask that is used to render a template and return the result as a response to a request. It takes the name of the template file as an argument and any additional data that should be passed to the template.
# 
# Here is an example of how the render_template() function can be used in Flask:

# In[ ]:


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Some code here to retrieve data
    data = ...
    return render_template('index.html', data=data)


# In this example, the index() function is a route in the Flask application that returns a response containing a rendered template. The render_template() function is used to render the index.html template file, and the data variable is passed as an argument to the template.
# 
# Overall, templates are an essential feature of Flask that enable developers to create dynamic web pages that can display different content based on various factors, and the render_template() function is used to render these templates and return them as a response to a request.

# #### Q5. Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.

# In[13]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


# ![test1111.PNG](attachment:test1111.PNG)

# In[ ]:




