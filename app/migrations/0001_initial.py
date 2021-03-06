# Generated by Django 3.0 on 2019-12-23 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mst_Post_Statuses',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('is_enabled', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(verbose_name='date published')),
                ('modofied', models.DateTimeField(verbose_name='date published')),
                ('post_status_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Mst_Post_Statuses')),
            ],
        ),
    ]
