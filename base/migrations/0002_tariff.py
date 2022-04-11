# Generated by Django 3.0 on 2022-04-01 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttoend', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tariffs', to='base.Train')),
            ],
        ),
    ]
