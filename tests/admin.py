from django.contrib import admin
from .models import Category,Title,Question,Choice,Result

# Register your models here.

admin.site.site_header = 'Alpha Admin'
admin.site.site_title = 'Alpha Area'
admin.site.index_title = 'Welcome to the Alpha Area'
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['title']}),
    ('Question Name',{'fields':['question_text']}),]

    inlines = [ChoiceInline]    

admin.site.register(Question,QuestionAdmin)    

class ResultInline(admin.TabularInline):
    model = Result
    extra=5

class TitleAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['category']}),
    ('Title Name',{'fields':['title_name']}),
    ('Image',{'fields':['img']}),]

    inlines =[ResultInline]   

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Category)
admin.site.register(Title,TitleAdmin)

