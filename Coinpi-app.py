from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/coin", methods=["GET"])
def coin_info():

    return jsonify({
        "name": "Diamond π Coin",
        "symbol": "π",
        "type": "diamond",
        "status": "online"
    })


@app.route("/api/coin/rotate", methods=["POST"])
def rotate_coin():

    data = request.get_json(silent=True) or {}

    return jsonify({
        "success": True,
        "message": "Coin rotation received",
        "symbol": data.get("symbol", "π"),
        "action": data.get("action", "rotate")
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
