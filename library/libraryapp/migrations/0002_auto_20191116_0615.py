# Generated by Django 2.2.7 on 2019-11-16 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(help_text='enter th author name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='enter the name of category', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='category_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Category'),
            preserve_default=False,
        ),
    ]