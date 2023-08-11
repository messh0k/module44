from django.db import models


class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)

    # Описание товара/информация о товаре
    description = models.TextField('описание')

    # Цена
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    auction = models.BooleanField('торг', help_text='Отметьте, уместен ли торг')

    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'

    # Имя продавца + контакты

    # Актуальность объявления

    # Количество товара

    # Возможен ли обмен

    # Адрес продажи/обмена

    # Б/У товар или нет

    # Возможность взять в долг
