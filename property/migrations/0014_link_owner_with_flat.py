from django.db import migrations


def link_owner_with_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    owners = Owner.objects.all()


    for owner in owners:
        owned_flats = list(flats.filter(owner=owner.name, owner_pure_phone=owner.owner_pure_phone))
        owner.flats.set(owned_flats)


class Migration(migrations.Migration):
    dependencies = [
        (('property', '0013_fill_owner_table')),
    ]

    operations = [
        migrations.RunPython(link_owner_with_flat)
    ]
