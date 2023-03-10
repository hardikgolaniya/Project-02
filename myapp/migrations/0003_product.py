# Generated by Django 4.1.5 on 2023-01-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_desc', models.TextField()),
                ('product_pic', models.ImageField(upload_to='product_pic/')),
            ],
        ),
    ]
