from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm  # import the LoginForm class


@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'Miguel'}  # fake user
  posts = [  # fake array of posts
    {
      'author': {
        'nickname': 'John',
        'avatar': '/static/user.png'
      },
      'body': 'Beautiful day in Portland!'
    },
    {
      'author': {
        'nickname': 'Susan',
        'avatar': '/static/user.png'
      },
      'body': 'The Avengers Movie was so cool!'
    }
  ]
  return render_template(
    template_name_or_list='index.html',
    title='Home',
    user=user,    # variable user is used on index
    posts=posts   # variable posts is used in index
  )

                   # methods tells Flask that this view function accepts GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()  # instantiated an object called form from the LoginForm class
  if form.validate_on_submit():
    # flash shows a message on the next page presented to the user
    flash('Login requested for OpenID="%s", remember_me=%s' %
          (form.openid.data, str(form.remember_me.data)))
    return redirect('/index')
  return render_template(
    template_name_or_list='login.html',
    title='Sign In',
    form=form,  # variable form is used in login
    providers=app.config['OPENID_PROVIDERS']
  )
