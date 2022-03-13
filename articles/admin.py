from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = list()
        [count.append(form.cleaned_data['is_main']) for form in self.forms]
        counter = sum(count)
        if counter > 1:
            raise ValidationError('Вы выбрали больше одного тега в качестве основного')
        elif counter == 0:
            raise ValidationError('Вы не выбрали ни одного тега в качестве основного')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
