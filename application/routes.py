from flask import render_template, request

from application import app
from application.forms import BasicForm, searchForm

# needed to connect to database
from application.data_provider_service import DataProviderService
# instantiating an object of DataProviderService
DATA_PROVIDER = DataProviderService()

@app.context_processor
def base():
    form = searchForm()
    return dict(form=form)


@app.route('/search', methods=['POST'])
def search():
    form = searchForm()
    posts = Posts.query
    if form.validate_on_submit():
        post.searched = form.searched.data

        posts = posts.filter(posts.content.like('%' + post.searched ))
        posts = posts.order_by(posts.title).all()

        return render_template(
            "search.html",
            form=form,
            searched=post.searched,
            posts = posts)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/reviews', methods=['GET'])
def reviews():
    all_people = DATA_PROVIDER.get_recipe()
    return render_template('reviews.html', title="Reviews", people=all_people)


# #use base html template
@app.route("/welcome/<name>/")
def welcome(name):
    return render_template('welcome.html', name=name, group='Everyone')


@app.route('/contactus')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')


@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html', title="About me")


@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='My Favourites', my_list=['books','swimming','hiking','eating'])


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
            new_recipe_id = DATA_PROVIDER.add_user_review(name, recipe, comment)
            success = 'Person with ID ' + str(new_recipe_id) + ' was created. Thank you!'
            return render_template('success.html', success_message=success)
    return render_template('new_review.html', title='Review', form=form, message=error)


