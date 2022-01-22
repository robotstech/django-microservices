# Generated by Django 3.2 on 2022-01-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('board_id', models.BigIntegerField(unique=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('image_id', models.BigIntegerField(unique=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='comments.comment')),
            ],
            options={
                'unique_together': {('image_id', 'comment')},
            },
        ),
    ]