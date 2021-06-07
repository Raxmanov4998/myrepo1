from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, URL, InputRequired, Regexp, Length
import re

def is_valid_phone(number):
    regex = re.compile(
        
        r"""^(\+?1)?[-. ]?\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})$"""
         )# A------AB----BC-----------CD----DE-----EF----FG------G        
        
          # A: (only at the beginning) +1 or 1. Optional
          # B: dash or dot or space.  Optional 
          # C: (nnn) or nnn, n - natural numbers. Necessary
          # D: dash or dot or space.  Optional
          # E: nnn, n - natural numbers. Necessary
          # F: dash or dot or space.  Optional
          # G: (only at the end) nnnn, n - natural numbers. Necessary
                        
    return regex.match(number)

state_choices = [
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]


genres_choices = [
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[ DataRequired(), Length(max=200) ]
    )
    city = StringField(
        'city', validators=[ DataRequired(), Length(max=200) ]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[ DataRequired(), Length(max=200) ]
    )
    phone = StringField(
        'phone', validators=[ InputRequired(), Length(max=200) ]
    )

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Invalid phone.')
            return False
        # if pass validation
        return True 

    image_link = StringField(
        'image_link', validators=[ URL(), Length(max=500) ]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction        #done
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[
        DataRequired(),
        
        Regexp(
        "(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?", 
       # A----------------------AB-------BC------------CD--------------DE----------EF-------------FG---------------------------GH--------H 
         
       # A: http://  or  https://    Optional
       # B: www. (dot = any character)  Optional
       # C: facebook.com/     Necessary
       # D: any word character (any times) and #!/   Optional
       # E: pages/   Optional
       # F: ? any word character - (any times) and /   Optional
       # G: profil.php?id= and any digit and dot (any times)   Optional
       # H: any word character and dash (any times)
       
       message="The correct format for the facebook link was not correct"
       ),
        
        Length(max=500)
        ]
    )
    website_link = StringField(
        'website_link', validators=[ URL(), Length(max=500) ]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description', validators=[ DataRequired(), Length(max=2000) ]
    )



class ArtistForm(Form):
    name = StringField(
        'name', validators=[ DataRequired(), Length(max=200) ]
    )
    city = StringField(
        'city', validators=[ DataRequired(), Length(max=200) ]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
        # TODO implement validation logic for state     #done
        'phone', validators=[ InputRequired(), Length(max=200) ]
    )

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Invalid phone.')
            return False
        # if pass validation
        return True

    image_link = StringField(
        'image_link', validators=[ URL(), Length(max=500) ]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
    facebook_link = StringField(
        # TODO implement enum restriction   # done
        'facebook_link', validators=[
        DataRequired(),
        
        Regexp(
        "(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?", 
       # A----------------------AB-------BC------------CD--------------DE----------EF-------------FG---------------------------GH--------H 
         
       # A: http://  or  https://    Optional
       # B: www. (dot = any character)  Optional
       # C: facebook.com/     Necessary
       # D: any word character (any times) and #!/   Optional
       # E: pages/   Optional
       # F: ? any word character - (any times) and /   Optional
       # G: profil.php?id= and any digit and dot (any times)   Optional
       # H: any word character and dash (any times)
       
       message="The correct format for the facebook link was not correct"
       ),
        
        Length(max=500)
        ]
    )

    website_link = StringField(
        'website_link', validators=[ URL(), Length(max=500) ]
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description', validators=[ DataRequired(), Length(max=2000)]
     )

