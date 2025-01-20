from flask import Flask,redirect,request,render_template,jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return "<H1>Hello</H1>"

if __name__=="__main__":
    app.run(debug=True)