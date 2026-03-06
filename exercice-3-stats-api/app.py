from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/stats', methods=['POST'])
def calculate_stats():
    numbers = request.json.get('numbers', [])
    if not numbers:
        return jsonify({'error': 'No data provided'}), 400

    count = len(numbers)
    total = sum(numbers)
    average = total / count if count else None

    result = {
        'count': count,
        'sum': total,
        'average': average,
        'min': min(numbers),
        'max': max(numbers)
    }
    return jsonify(result)


@app.route('/api/stats/median', methods=['POST'])
def calculate_median():
    data = sorted(request.json.get('numbers', []))
    n = len(data)

    if n == 0:
        return jsonify({'error': 'No data provided'}), 400

    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]

    return jsonify({'median': median})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)