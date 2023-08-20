# Generated by Django 4.0.4 on 2022-08-18 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_profile_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acceptance', models.BooleanField(default=False)),
                ('Reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reciever', to='panel.profile')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to='panel.profile')),
            ],
        ),
    ]
