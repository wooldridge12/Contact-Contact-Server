# Generated by Django 3.2.7 on 2021-09-16 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactContactapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contact_user',
            new_name='reciever',
        ),
        migrations.RemoveField(
            model_name='message',
            name='battle_buddy',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mesages', to='contactContactapi.contactuser'),
            preserve_default=False,
        ),
    ]
