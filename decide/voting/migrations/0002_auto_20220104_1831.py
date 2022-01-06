# Generated by Django 2.2.5 on 2022-01-04 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScoreQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='binaryvoting',
            name='type',
            field=models.CharField(choices=[('BV', 'BinaryVoting')], default='BV', max_length=2),
        ),
        migrations.AddField(
            model_name='voting',
            name='type',
            field=models.CharField(choices=[('V', 'Voting')], default='V', max_length=2),
        ),
        migrations.CreateModel(
            name='ScoreVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('tally', models.Field(blank=True, default=[], null=True)),
                ('postproc', models.Field(blank=True, default=[], null=True)),
                ('type', models.CharField(choices=[('SV', 'ScoreVoting')], default='SV', max_length=2)),
                ('auths', models.ManyToManyField(related_name='scorevoting', to='base.Auth')),
                ('pub_key', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scorevoting', to='base.Key')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scorevoting', to='voting.ScoreQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreQuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('option', models.PositiveIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='voting.ScoreQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('tally', models.Field(blank=True, default=[], null=True)),
                ('postproc', models.Field(blank=True, default=[], null=True)),
                ('type', models.CharField(choices=[('MV', 'MultipleVoting')], default='MV', max_length=2)),
                ('auths', models.ManyToManyField(related_name='multiplevoting', to='base.Auth')),
                ('pub_key', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='multiplevoting', to='base.Key')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiplevoting', to='voting.MultipleQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleQuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('option', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='voting.MultipleQuestion')),
            ],
        ),
    ]
