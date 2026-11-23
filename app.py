from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = "carrie-pie-2026"

@app.route("/webhook", methods=["GET"])
def verify():
    if (request.args.get("hub.mode") == "subscribe"
            and request.args.get("hub.verify_token") == VERIFY_TOKEN):
        return request.args.get("hub.challenge"), 200
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def incoming():
    print(request.get_json())
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
