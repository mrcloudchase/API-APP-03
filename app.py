from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/scripteditor', methods=['GET'])
def get_endpoint_2():
    endpoint_name = request.endpoint
    return jsonify({"endpoint": endpoint_name, "branch": "uat"})

if __name__ == '__main__':
    app.run(debug=True)
