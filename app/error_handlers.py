from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error"}), 500
