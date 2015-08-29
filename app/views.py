from app import app, db
from flask import render_template, url_for

# Models
class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	# password
	about = db.Column(db.Text)
	pages = db.relationship('Page', backref='author')
	posts = db.relationship('Post', backref='author')
	social_icons = db.relationship('SocialIcon', backref='user')

	def __repr__(self):
		return '<User %r>' % self.username

class Page(db.Model):
	__tablename__ = "pages"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, index=True)
	description = db.Column(db.Text)
	image = db.Column(db.Boolean, default=False)
	posts = db.relationship('Post', backref='page')
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return '<Page %r>' % self.name

class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True)
	body = db.Column(db.Text)
	image = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))

	def __repr__(self):
		return '<Post %r>' % self.title

# The css_value references the font-awesome value for the icon
class SocialIcon(db.Model):
	__tablename__ = "social_icons"
	id = db.Column(db.Integer, primary_key=True)
	href = db.Column(db.String(140))
	css_value = db.Column(db.String(32))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return '<SocialIcon %r>' % self.href


# Views
@app.route('/')
def index():
	user = User.query.first()
	pages = Page.query.all()
	return render_template('index.html', user=user, pages=pages)


@app.route('/page/<name>')
def page(name):
	pages = Page.query.all()
	posts = Post.query.all()
	social_icons = SocialIcon.query.all()
	return render_template('page.html', name=name, pages=pages, posts=posts, social_icons=social_icons)