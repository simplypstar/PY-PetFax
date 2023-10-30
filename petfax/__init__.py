from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # return the app 
    return app
