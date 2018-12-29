# Generated by Django 2.1.4 on 2018-12-27 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_classroom_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField()),
                ('exam_grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=2)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom')),
            ],
            options={
                'ordering': ('name', 'exam_grade'),
            },
        ),
    ]