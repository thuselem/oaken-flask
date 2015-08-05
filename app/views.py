from app import app
from flask import render_template, url_for


interests = {1 : {'area':'code', 'about': 'This is the code page', 'color': 'red', 'FKUserId': 1}, 
			 2 : {'area':'text', 'about': 'This is the text page', 'color': 'blue', 'FKUserId': 1},
			 3 : {'area':'music', 'about': 'This is the music page', 'color': 'green', 'FKUserId': 1}
		}

users = {1: {'name': 'admin',' password': 'default'}}

posts = {1: {'title': 'Python', 'text': 'I like Python', 'FK_IntrestId': 1},
		 2: {'title': 'Flask', 'text': 'This is built on Flask', 'FK_IntrestId': 1},
		 3: {'title': 'Blogging', 'text': 'I write blogposts', 'FK_IntrestId': 2},
		 1: {'title': 'Cello', 'text': 'I play the Cello', 'FK_IntrestId': 3},
		 1: {'title': 'Audio Production', 'text': 'I produce my own music', 'FK_IntrestId': 3}
	}

@app.route('/')
def index():
	return render_template('index.html', interests=interests)

@app.route('/interest/<area>')
def interest(area):
	return render_template('interest.html', interests=interests)