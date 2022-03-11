from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Article_topic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Раздел')
    relationships = models.ManyToManyField(Article, through='Relationship')

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self):
        return self.name


class Relationship(models.Model):
    article_topics = models.ForeignKey(Article_topic, on_delete=models.CASCADE, related_name='scopes')
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
