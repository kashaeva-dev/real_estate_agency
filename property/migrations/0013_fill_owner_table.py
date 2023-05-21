from django.db import migrations


def fill_owners_from_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        Owner.objects.get_or_create(
            name=flat.owner,
            owner_pure_phone=flat.owner_pure_phone,
            defaults={
                'owners_phonenumber': flat.owners_phonenumber,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        (('property', '0012_auto_20230517_2155')),
    ]

    operations = [
        migrations.RunPython(fill_owners_from_flats),
    ]
