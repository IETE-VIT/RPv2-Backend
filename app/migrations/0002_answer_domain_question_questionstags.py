# Generated by Django 3.2.8 on 2021-11-09 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=255, unique=True)),
                ('quiz_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_type', models.IntegerField(choices=[(0, 'MCQ'), (1, 'LONG')], default=0, verbose_name='Question Type')),
                ('mark_each', models.IntegerField(default=0, verbose_name='Mark for the Question')),
                ('ques_main', models.CharField(max_length=255, verbose_name='Question')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='domain', to='app.domain')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='QuestionsTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(choices=[('DOMAIN', 'DOMAIN'), ('ENGLISH', 'ENGLISH')], max_length=100, verbose_name='Tags')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tag', to='app.question')),
            ],
            options={
                'verbose_name': 'Tags',
                'verbose_name_plural': 'Tags',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='app.question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
    ]