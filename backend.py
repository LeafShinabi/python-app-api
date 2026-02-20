
from flask import Flask, jsonify, request

app = Flask(__name__)

# This is a 'Route'. The frontend will 'hit' this URL to get data.
@app.route('/api/data', methods=['GET'])
def get_info():
    user_input = request.args.get('name', 'Stranger')
    # Returning a Dictionary (which Flask turns into JSON)
    return jsonify({
        "status": "success",
        "message": f"Server processed: {user_input}",
        "data_length": len(user_input)
    })

if __name__ == '__main__':
    # Running on port 5000
    app.run(port=5000, debug=True)