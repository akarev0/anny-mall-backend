# Generated by Django 3.1.2 on 2020-11-28 12:13

import bboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products_in_basket', models.PositiveIntegerField(default=0)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая стоимость заказа')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('size', models.IntegerField(verbose_name='Размер')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, upload_to=bboard.models.image_directory_path, verbose_name='Фото')),
                ('material', models.CharField(blank=True, max_length=255, null=True, verbose_name='Материал')),
                ('season', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сезон')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bboard.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказ')),
                ('buying_type', models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип заказа')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа')),
                ('basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard.basket', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='bboard.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='customer_orders', to='bboard.Order', verbose_name='Заказы'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='BasketProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая стоимость заказа')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='bboard.basket', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bboard.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bboard.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard.customer', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_basket', to='bboard.BasketProduct'),
        ),
    ]
