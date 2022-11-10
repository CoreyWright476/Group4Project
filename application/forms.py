from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm


class BasicForm(FlaskForm):
    # instantiating various input fields
    name = StringField(' Name')
    recipe = StringField('Recipe')
    comment = StringField('Comment')
    submit = SubmitField('Add Review')

class searchForm(FlaskForm):
    searched = StringField("Searched")
    submit = SubmitField('submit')
