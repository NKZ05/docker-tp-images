from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/stats', methods=['POST'])
def calculate_stats():
    data = request.json.get('numbers', [])
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = {
        'count': len(data),
        'sum': sum(data),
        'average': sum(data) / len(data),
        'min': min(data),
        'max': max(data)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)