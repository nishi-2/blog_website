from .ml_blog_routes import ml_bp

def machine_learning_blueprints(app):
    app.register_blueprint(ml_bp)