# Generated by Django 3.1.3 on 2021-01-28 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('atm_py', '0002_transaction_dummy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_inq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='transaction_dummy',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='DataClass',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transaction_dummy',
        ),
    ]