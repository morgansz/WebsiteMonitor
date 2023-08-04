from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define website model
class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    last_checked = db.Column(db.DateTime, nullable=False)
    last_changed = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Website %r>' % self.url
    
 # Define notification model
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)
    website = db.relationship('Website', backref=db.backref('notifications', lazy=True))
    status = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Notification %r>' % self.status

 # Define user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email
