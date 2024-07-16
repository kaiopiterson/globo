# api/routes.py
from flask import request, jsonify
from . import api_bp

comments = []

@api_bp.route('/api/comment/new', methods=['POST'])
def add_comment():
    data = request.get_json()
    comments.append(data)
    return jsonify({"message": "Comment added successfully!"}), 201

@api_bp.route('/api/comment/list/<int:content_id>', methods=['GET'])
def list_comments(content_id):
    filtered_comments = [c for c in comments if c['content_id'] == content_id]
    return jsonify(filtered_comments), 200

