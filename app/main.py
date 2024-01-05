from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  print("Hello, World!")

if __name__ == "__main__":
    app.run(threaded=True)
