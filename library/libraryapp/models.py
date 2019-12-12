from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=100,help_text="enter th author name")

    class Meta:
        verbose_name_plural="author"

    def __str__(self):
         return self.author_name

class Category(models.Model):
    category_name = models.CharField(max_length=100,help_text="enter the name of category")

    def __str__(self):
        return self.category_name


class Book(models.Model):
        book_name = models.CharField(max_length=100, help_text="enter the name of the book")
        book_price = models.IntegerField(help_text="enter the price of book")
        isbn_number = models.CharField(max_length=100)
        author_name=models.ForeignKey(Author, on_delete=models.CASCADE)
        category_name=models.ForeignKey(Category, on_delete=models.CASCADE)

        def __str__(self):
            return self.book_name

class Member(models.Model):
    member_fname = models.CharField(max_length=100,help_text="enter the member fname")
    member_lname = models.CharField(max_length=100, help_text="enter the member lname")
    member_phonenumber = models.IntegerField(help_text="enter the phonenumber")
    member_emailid = models.EmailField(max_length=100, help_text="enter the mail id")

    def __str__(self):
        return self.member_fname

class Record(models.Model):
    issue_date = models.DateField()
    return_date= models.DateField()
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    member_fname = models.ForeignKey(Member,on_delete=models.CASCADE)



    def __str__(self):
        return self.member_fname





        def upper(self):
            return  self.book_name.upper()





