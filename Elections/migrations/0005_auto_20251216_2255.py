from django.db import migrations

def create_groups(apps, schema_editor):
    # Get the historical version of the Group model
    Group = apps.get_model('auth', 'Group')
    groups = ['Admin', 'ElectionManager', 'Voter']
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)

class Migration(migrations.Migration):
    dependencies = [
        ('Elections', '0004_alter_vote_voter'),  # replace with your last migration file before this
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
