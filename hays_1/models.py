from hays_1 import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)  # unique=True
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    primary_email = db.Column(db.String(64))

    emails = db.relationship("OtherEmail", backref="contact", lazy="dynamic")

    def __repr__(self):
        return f"< Contact {self.username} >"


class OtherEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    contact_id = db.Column(db.Integer, db.ForeignKey("contact.id"))

    def __repr__(self):
        return f"<Post {self.address}>"
