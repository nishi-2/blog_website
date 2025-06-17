from .python_blog_routes import python_bp

def python_blueprints(app):
    app.register_blueprint(python_bp)