
from base import app
from base.com.controller.candidate_controller import candidate_blueprint

app.register_blueprint(candidate_blueprint)

if __name__ == "__main__":
    app.run(debug=True)