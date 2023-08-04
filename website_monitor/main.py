from flask import Flask
from models import db
from views import website_view, email_view
from scheduler import start_scheduler

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(website_view)
app.register_blueprint(email_view)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        start_scheduler(db)
    app.run()
