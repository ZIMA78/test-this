from bottle import route, run
def tell_me_your_secret():
    return 42
@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    return {
    "result": top / bottom,
    "error": None,
    "secret": tell_me_your_secret()
 }
if __name__ == "__main__":

    print("[server] __name__ =", __name__)
    run(host="localhost", port="8080")

