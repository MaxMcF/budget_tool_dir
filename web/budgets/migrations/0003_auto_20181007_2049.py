# Generated by Django 2.1.2 on 2018-10-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_auto_20181004_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='action_type',
            field=models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAW', 'Withdraw')], max_length=16),
        ),
    ]
