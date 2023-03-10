# Generated by Django 4.1.5 on 2023-02-12 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NodeRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='tree.node')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.node')),
            ],
        ),
    ]
