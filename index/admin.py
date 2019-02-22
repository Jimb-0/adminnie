from django.contrib import admin
from index.models import Login_Model, Quote, Insurance, Comment

admin.site.register(Login_Model)
admin.site.register(Quote)
admin.site.register(Insurance)
admin.site.register(Comment)

# Register your models here.
