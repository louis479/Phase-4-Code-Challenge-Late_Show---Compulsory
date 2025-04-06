

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Apperance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number,
            "appearances": [appearance.to_dict() for appearance in self.appearances]
        }
    
class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }
    
