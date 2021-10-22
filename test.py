from flask import Flask

app = Flask(__name__)

# @app.route("/hello")
# def test_hello():
#     return "Hello Flask"
#     host_addr = "127.0.0.1"
#     port_num = ""
#     app.run(host=host_addr, port=port_num)

@app.route("/<int:num>")
def hello(num):
    return "Hello world"