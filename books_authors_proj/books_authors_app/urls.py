from django.urls import path
from . import views

urlpatterns = [
	# Books
	path('', views.index),
	path('add_book', views.add_book),
	path('books/<int:book_id>', views.show_book),
	path('add_author/<int:book_id>', views.add_author_to_book),

	# Authors
	path('authors', views.authors),
	path('author/add_author', views.add_author),
	path('author/<int:author_id>', views.show_author),
	path('add_book/<int:author_id>', views.add_book_to_author)
]
