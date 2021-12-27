############------------ IMPORTS ------------############
from app import create_app


############------------ GLOBAL VARIABLE(S) ------------############
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)