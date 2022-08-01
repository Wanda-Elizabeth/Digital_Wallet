# Generated by Django 4.0.6 on 2022-08-01 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='Customer_id',
            new_name='customer_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='destination_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.account'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='guaranter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.third_party'),
        ),
        migrations.AlterField(
            model_name='third_party',
            name='type',
            field=models.CharField(max_length=6),
        ),
    ]
