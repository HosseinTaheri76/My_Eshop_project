# Generated by Django 3.2.8 on 2022-01-08 04:04

import articles.uploaders
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='نام برچسب')),
                ('slug', models.SlugField(help_text='نام برچسب را وارد کنید به جای فاصله از آندرلاین استفاده کنید.', max_length=100, unique=True, verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_name', models.CharField(max_length=75, unique=True, verbose_name='نام دسته بندی فارسی')),
                ('en_name', models.CharField(max_length=75, unique=True, verbose_name='نام دسته بندی انگیلیسی')),
                ('slug', models.SlugField(help_text='نام دسته بندی انگیلیسی را وارد کنید به جای فاصله از آندرلاین استفاده کنید.', max_length=100, unique=True, verbose_name='اسلاگ')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='articles.category', verbose_name='زیر شاخه ی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=articles.uploaders.article_image_uploader, verbose_name='عکس اصلی خبر')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='بدنه مقاله')),
                ('date_published', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('slug', models.SlugField(help_text='نام برچسب را وارد کنید به جای فاصله از آندرلاین استفاده کنید.', max_length=100, unique=True, verbose_name='اسلاگ')),
                ('view_count', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.category', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(blank=True, to='articles.ArticleTag', verbose_name='برچسب ها')),
            ],
        ),
    ]
