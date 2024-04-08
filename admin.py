from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=True)


@app.route('/books')
def books():
    books = [{'name': 'book1', 'author': 'auth1', 'cover': 'http://images.clipartpanda.com/books-20clip-20art-books-clipart.jpg'}, {'name': 'book2',
                                                                                                                                    'author': 'auth2', 'cover': 'http://images.clipartpanda.com/books-20clip-20art-books-clipart.jpg'}, {'name': 'book3', 'author': 'auth3', 'cover': 'http://images.clipartpanda.com/books-20clip-20art-books-clipart.jpg'}]
    return render_template('books.html', books=books)


app.run(debug=True)
