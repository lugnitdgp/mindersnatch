# Generated by Django 2.1.5 on 2020-04-01 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0025_auto_20200401_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situation',
            name='option_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option1', to='mindapp.option'),
        ),
        migrations.AlterField(
            model_name='situation',
            name='option_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option2', to='mindapp.option'),
        ),
        migrations.AlterField(
            model_name='situation',
            name='option_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option3', to='mindapp.option'),
        ),
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]
