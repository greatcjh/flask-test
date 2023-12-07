from flask import Flask, request, render_template
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core import xray_recorder

app = Flask(__name__)

xray_recorder.configure(service='ft')
XRayMiddleware(app, xray_recorder)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/mypage')
def mypage():
   return 'This is My Page! HaHa 2!'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)