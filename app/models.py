from django.db import models


class PageVersion(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    content = models.TextField(verbose_name='Контент', )
    current_version = models.PositiveIntegerField(verbose_name='Поточна версія', )
    active_version = models.PositiveIntegerField(verbose_name='Активна версія', default=1)

    def __str__(self):
        return f'{self.title}, Версія: {self.current_version}'

    class Meta:
        verbose_name = 'Поточна версія'
        verbose_name_plural = 'Поточні версії'
        ordering = ['current_version']


class WikiPage(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    versions = models.ForeignKey(PageVersion, on_delete=models.CASCADE, verbose_name='Версії', default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сторінка'
        verbose_name_plural = 'Сторінки'
        ordering = ['title']



