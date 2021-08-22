# Generated by Django 3.2.5 on 2021-08-22 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ediary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('duration_hrs', models.PositiveIntegerField()),
                ('duration_min', models.PositiveIntegerField()),
                ('duration_sec', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('C', 'Cardio'), ('S', 'Strength')], default='C', max_length=1)),
                ('exercise_name', models.CharField(choices=[('RUN', 'Run'), ('SWIM', 'Swim'), ('WALK', 'Walk'), ('CYCLE', 'Cycle')], default='RUN', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='strengthdiary',
            name='type',
        ),
        migrations.AddField(
            model_name='exerciselocation',
            name='location_type',
            field=models.CharField(choices=[('IN', 'Indoor'), ('OUT', 'Outdoor')], default='IN', max_length=3),
        ),
        migrations.DeleteModel(
            name='CardioDiary',
        ),
        migrations.DeleteModel(
            name='ExerciseType',
        ),
        migrations.DeleteModel(
            name='StrengthDiary',
        ),
        migrations.AddField(
            model_name='activities',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ediary.exercise'),
        ),
        migrations.AddField(
            model_name='activities',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ediary.exerciselocation'),
        ),
        migrations.AddField(
            model_name='activities',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ediary.users'),
        ),
    ]