import form as form
from flask import render_template, request, flash

from application import app
from application.forms import BasicForm, RecipeForm

# needed to connect to database
from application.data_provider_service import DataProviderService
# instantiating an object of DataProviderService
DATA_PROVIDER = DataProviderService()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Welcome to our world foods')

@app.route('/english')
def english():
    return render_template('English_recipies.html', title='English recipes')



@app.route('/japanese')
def japanese():
    return render_template('Japanese_recipies.html', title='Japanese recipes')


@app.route('/indian')
def indian():
    return render_template('Indian_recipies.html', title='Indian recipies')


@app.route('/contactus')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')


@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html', title="About me")


@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='My Favourites', my_list=['books','swimming','hiking','eating'])



@app.route('/reviews', methods=['GET'])
def reviews():
    all_people = DATA_PROVIDER.get_recipe()
    return render_template('reviews.html', title="Reviews", people=all_people)

@app.route('/new_review', methods=['GET', 'POST'])
def new_review():
    error = ""
    # instantiating an object of type BasicForm
    form = BasicForm()

    if request.method == 'POST':
        name = form.name.data
        recipe = form.recipe.data
        comment = form.comment.data
        if len(name) == 0 or len(recipe) == 0 or len(comment) == 0:
            error = "Please supply - name , recipe and comment"
        else:
            new_review_id = DATA_PROVIDER.add_user_review(name, recipe, comment)
            success = 'Person with ID ' + str(new_review_id) + ' was created. Thank you!'
            return render_template('success.html', success_message=success)
    return render_template('new_review.html', title='Review', form=form, message=error)

@app.route('/new_recipes', methods=['GET', 'POST'])
def recipe():
    error = ""
    # instantiating an object of type BasicForm
    form = RecipeForm()
    if request.method == 'POST':
        name = form.name.data
        rec_name = form.recipe_name.data
        rec_ins = form.recipe.data
        if len(name) == 0 or len(rec_name) == 0 or len(rec_ins) == 0:
            error = "Please supply your name the recipe and the recipe."
        else:
            new_user_recipe_ID = DATA_PROVIDER.add_user_recipe(name, rec_name, rec_ins)
            success = 'Recipe ID ' + str(new_user_recipe_ID) + ' was created. Thank you!'
            return render_template('new_recipies.html', message=success, form=form)

    return render_template('new_recipies.html', title='new recipies', form=form, message=error)

@app.route('/user_recipes', methods=['GET'])
def user_recipes():
    all_people = DATA_PROVIDER.geet_recipe()
    return render_template('uploaded_recipes.html', title="Added recipes", people=all_people)

# @app.route('/name', methods=['GET', 'POST'])
# def name():
#     name = None
#     form = PostForm()
#     #Validate form, if someone submits their name to the form it will assign to the variable below
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#         flash("Form Submitted Successfully!")
#
#     return render_template("name.html",
#                             name = name,
#                             form = form)

