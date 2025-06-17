from .dl_blog_routes import dl_bp

def deep_learning_blueprints(app):
    app.register_blueprint(dl_bp)