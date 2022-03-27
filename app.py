from flask import Flask
from modules import users, investments

app = Flask(__name__)
app.register_blueprint(users.devices_bp)
app.register_blueprint(investments.devices_bp)

if __name__ == "__main__":
  app.run()
