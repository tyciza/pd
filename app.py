
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check')
def check_values():
    try:
        x = float(request.args.get('x', 0))
        y = float(request.args.get('y', 0))
        result = "greater than 100" if x + y > 100 else "less or equal to 100"
        return jsonify({"x": x, "y": y, "decision": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run()
