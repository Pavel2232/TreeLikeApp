from django.db import models


class Page(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название страницы'
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Фрагмент URL-адреса',
        blank=True
    )
    url = models.URLField(
        max_length=10000,
        verbose_name='Полный URL-адрес',
        blank=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родительская страница',
        null=True,
        blank=True
    )

    def get_full_url(self):
        url_parts = [self.slug]
        parent = self.parent
        while parent:
            url_parts.insert(0, parent.slug)
            parent = parent.parent

        full_url = '/'.join(filter(None, url_parts))

        full_url = full_url.strip('/')

        if full_url:
            full_url = '/' + full_url + '/'
        else:
            full_url = '/'
        return full_url

    def save(self, *args, **kwargs):
        self.url = self.get_full_url()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name
