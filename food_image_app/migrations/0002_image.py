# Generated by Django 3.2.12 on 2022-03-24 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_image_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_by', models.CharField(max_length=100)),
                ('food_group', models.CharField(choices=[('Fruit', 'Fruit'), ('Vegetable', 'Vegetable'), ('Grain', 'Grain'), ('Dairy', 'Dairy'), ('Confectionery', 'Confectionery'), ('Unknown', 'Unknown')], max_length=100)),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kid_food_images', to='food_image_app.kid')),
            ],
        ),
    ]