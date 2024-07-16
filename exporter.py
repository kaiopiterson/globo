from flask import Flask, Response
import requests
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

# Defina a métrica
comment_count = Gauge('comment_count', 'Number of comments')
comments = Gauge('comments', 'Details of comments', ['email', 'comment', 'content_id', 'timestamp'])

@app.route('/metrics')
def metrics():
    try:
        response = requests.get('http://172.23.64.196:30007/api/comment/list/1')
        if response.status_code == 200:
            data = response.json()
            comment_count.set(len(data))
            for comment in data:
                comments.labels(email=comment['email'], comment=comment['comment'], content_id=comment['content_id'], timestamp=comment['timestamp']).set(1)
        else:
            comment_count.set(0)
    except Exception as e:
        comment_count.set(0)
    
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
