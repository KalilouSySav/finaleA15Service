# Generated by Django 4.2.5 on 2023-10-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code_projet", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=1000)),
            ],
        ),
    ]
