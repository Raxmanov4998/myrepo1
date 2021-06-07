from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(500))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate   # done
    genres = db.Column(db.ARRAY(db.String()))
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(2000))
    shows = db.relationship('Show', backref=db.backref('venues', lazy=True), cascade="all, delete")

    def __repr__(self):
       return f'<Venue ID: {self.id}, name: {self.name}, shows: {self.shows}>'

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    genres = db.Column(db.ARRAY(db.String()))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(500))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate   # done
    website = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(2000))
    shows = db.relationship('Show', backref=db.backref('artist', lazy=True), cascade="all, delete")
    
    def __repr__(self):
        return f'<Artist ID:{self.id}, name:{self.name}, shows:{self.shows}>'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.   # done
class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer,db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    show_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Show artist_id: {self.artist_id}, venue_id: {self.venue_id} >'