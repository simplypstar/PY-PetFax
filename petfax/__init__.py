from flask import Flask

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # pets index route
    @app.route('/pets')
    def pets(): 
        return 'These are our pets available for adoption!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # return the app 
    return app
