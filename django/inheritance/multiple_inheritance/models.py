from django.db import models

class Piece(models.Model):
    pass

class Article(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)

    #부모랑 연결되는 piece_ptr이 만들게 됨 onetoone에서

class BookReview(Book, Article):
    pass