from django.db import migrations
import phonenumbers


def prettify_phone(phone):
    try:
        parsed_phone = phonenumbers.parse(phone, 'RU')
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

    if phonenumbers.is_valid_number(parsed_phone):
        pure_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
        return pure_phone
    else:
        return None


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        pure_phone = prettify_phone(flat.owners_phonenumber)
        flat.owner_pure_phone = pure_phone
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        (('property', '0009_auto_20230517_1915')),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone),
    ]
