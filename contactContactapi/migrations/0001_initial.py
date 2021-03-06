# Generated by Django 3.2.7 on 2021-09-10 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BattleBuddy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HelpSectionPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('is_helped', models.BooleanField(default=False)),
                ('contact_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.contactuser')),
            ],
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('contact_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.contactuser')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('created_on_date', models.IntegerField()),
                ('battle_buddy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.battlebuddy')),
                ('contact_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.contactuser')),
                ('help_section_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.helpsectionpost')),
            ],
        ),
        migrations.AddField(
            model_name='helpsectionpost',
            name='urg_button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.urgency'),
        ),
        migrations.AddField(
            model_name='battlebuddy',
            name='contact_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactContactapi.contactuser'),
        ),
    ]
