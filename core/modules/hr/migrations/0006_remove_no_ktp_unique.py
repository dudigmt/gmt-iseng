from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_employee_import_batch_employee_imported_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='no_ktp',
            field=models.CharField(max_length=16, blank=True, null=True),
        ),
    ]