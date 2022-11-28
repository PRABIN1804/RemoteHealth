

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=200)),
                ('employee_date_of_joining', models.CharField(max_length=50)),
                ('employee_gender', models.CharField(max_length=50)),
                ('employee_department', models.CharField(max_length=50)),
                ('employee_designation', models.CharField(max_length=200)),
                ('employee_address', models.CharField(max_length=200)),
                ('employee_contact', models.CharField(max_length=200)),
                ('employee_email', models.CharField(max_length=200)),
            ],
        ),
    ]
