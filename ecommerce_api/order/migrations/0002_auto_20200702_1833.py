# Generated by Django 2.1.11 on 2020-07-02 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
