from django.contrib import admin
from .models import Book,Author,Category,Member,Record
from django import forms

class AuthorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorAdminForm,self).__init__(*args, **kwargs)

    def clean(self):
        author=self.cleaned_data.get('author_name')
        if len(author) < 4:
            raise forms.ValidationError('please enter a valid name,name cannot be less than 4 character',code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(AuthorAdminForm,self).save(commit=commit)


class BookAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        price = self.cleaned_data.get('book_price')
        if price < 500:
            raise forms.ValidationError('please enter a valid price,price cannot be graterthan than 500 price',
                                        code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(BookAdminForm, self).save(commit=commit)




# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form=BookAdminForm
    list_display = ('book_name', 'book_price', 'isbn_number', 'author_name', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('book_name',)
    ordering = ('book_name',)



class AuthorAdmin(admin.ModelAdmin):
    form=AuthorAdminForm
    search_fields = ("author_name",)
    ordering = ("author_name",)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)



admin.site.register(Book, BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Member)
admin.site.register(Record)

