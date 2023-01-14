from flask import Flask,request, render_template
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os

import time 
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/login',methods = ['POST', 'GET'])
def my_link():
  print ('form submitted')
  sessionID = request.args.get('SessionID')
  name = request.args.get('NameClient')
  length = len(sessionID)
  sessionID = sessionID.replace('-', '')
  url = "https://join.zoho.com/assist-join?key=" + sessionID + "&language=en&email=" + name
  browser = webdriver.Edge(EdgeChromiumDriverManager().install())
  browser.get(url)
  browser.implicitly_wait(10)
  browser.executeScript("document.querySelector('.report-abuse-container').style.display = 'none';")
  browser.executeScript("document.querySelector('.cb-container').style.display = 'none';")
  return "check your downloads!!"

  

if __name__ == '__main__':
  app.run(debug=False, host="0.0.0.0", port=5000)