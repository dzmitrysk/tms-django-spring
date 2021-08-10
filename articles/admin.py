from django.contrib import admin

from articles.models import Article, Category, Author, ContactInfo, Edition


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(ContactInfo)
admin.site.register(Edition)

