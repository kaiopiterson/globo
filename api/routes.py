import logging
from flask import request, jsonify
from . import api_bp
from .models import Comment
from . import db

@api_bp.route('/api/comment/new', methods=['POST'])
def add_comment():
    try:
        logging.debug('Received request to add new comment')
        data = request.get_json()
        new_comment = Comment(email=data['email'], comment=data['comment'], content_id=data['content_id'])
        db.session.add(new_comment)
        db.session.commit()
        logging.debug('Comment added successfully')
        return jsonify({"message": "Comment added successfully!"}), 201
    except Exception as e:
        logging.error(f"Error adding comment: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500

@api_bp.route('/api/comment/list/<int:content_id>', methods=['GET'])
def list_comments(content_id):
    try:
        logging.debug(f'Received request to list comments for content_id: {content_id}')
        comments = Comment.query.filter_by(content_id=content_id).all()
        comments_list = [{"email": comment.email, "comment": comment.comment, "content_id": comment.content_id, "timestamp": comment.timestamp} for comment in comments]
        logging.debug('Comments listed successfully')
        return jsonify(comments_list), 200
    except Exception as e:
        logging.error(f"Error listing comments: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500
