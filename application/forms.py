from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


# inheritance
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm


class BasicForm(FlaskForm):
    # instantiating various input fields
    name = StringField(' Name', validators=[DataRequired()])
    recipe = StringField('Recipe', validators=[DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Add Review', validators=[DataRequired()])


class RecipeForm(FlaskForm):
    name = StringField("Whats your name?", validators=[DataRequired()])
    recipe_name= StringField("recipe name", validators=[DataRequired()])
    recipe=StringField("Enter your recipe", validators=[DataRequired()])
    submit = SubmitField('submit')


