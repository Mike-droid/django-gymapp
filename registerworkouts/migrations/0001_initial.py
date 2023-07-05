# Generated by Django 4.2.3 on 2023-07-05 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercises', '0001_initial'),
        ('workoutsessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('series', models.PositiveIntegerField()),
                ('repetitions', models.PositiveIntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercise')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workoutsessions.session')),
            ],
        ),
    ]
