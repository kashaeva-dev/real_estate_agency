from django.db import migrations
from django.db.models import Q


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    flats.update(new_building=Q(construction_year__gte=2015))


class Migration(migrations.Migration):
    dependencies = [
        (('property', '0003_flat_new_building'))
    ]

    operations = [
        migrations.RunPython(fill_new_building),
    ]
