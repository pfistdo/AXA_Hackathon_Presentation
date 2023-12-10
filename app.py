from flask import Flask, render_template

app = Flask(__name__)

# ###############################
# HTML Endpoints
# ###############################
@app.route("/")
def index():
    return render_template("index.html")


# ###############################
# Error Handler
# ###############################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html') # redirect to index.html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)