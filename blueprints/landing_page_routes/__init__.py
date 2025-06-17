from .general_routes import general_bp

def landing_page_register_blueprints(app):
    app.register_blueprint(general_bp)