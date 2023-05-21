from django.db import migrations


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    flats.objects.filter(construction_year__gte=2015).update(new_building=True)
    flats.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):
    dependencies = [
        (('property', '0003_flat_new_building')),
    ]

    operations = [
        migrations.RunPython(fill_new_building),
    ]
