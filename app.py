from flask import Flask, render_template

# referencing this file
app = Flask(__name__)

# set up routes with @route decorator
# this passes url string of route
@app.route('/')

#define function for route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

