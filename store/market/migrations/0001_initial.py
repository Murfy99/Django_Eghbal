# Generated by Django 4.2.9 on 2024-02-04 08:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_edit_date', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.category')),
            ],
        ),
    ]
