# Generated by Django 4.0 on 2021-12-22 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_title_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.category'),
        ),
    ]