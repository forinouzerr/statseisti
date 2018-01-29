# Generated by Django 2.0.1 on 2018-01-20 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connexion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresseip', models.CharField(blank=True, db_column='adresseIP', max_length=16, null=True)),
                ('systexploitation', models.CharField(blank=True, db_column='systExploitation', max_length=50, null=True)),
                ('datedebut', models.DateTimeField(blank=True, db_column='dateDebut', null=True)),
                ('duree', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('adresse', models.CharField(blank=True, max_length=100, null=True)),
                ('codepostal', models.CharField(blank=True, db_column='codePostal', max_length=10, null=True)),
                ('ville', models.CharField(blank=True, max_length=50, null=True)),
                ('pays', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pays', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialitecampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(blank=True, max_length=20, null=True)),
                ('campus', models.CharField(blank=True, max_length=25, null=True)),
                ('anneescolaire', models.CharField(blank=True, db_column='anneeScolaire', max_length=9, null=True)),
                ('ideleve', models.ForeignKey(blank=True, db_column='idEleve', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backoffice.Eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(blank=True, max_length=150, null=True)),
                ('anneescolaire', models.CharField(blank=True, db_column='anneeScolaire', max_length=20, null=True)),
                ('entreprise', models.CharField(blank=True, max_length=100, null=True)),
                ('codepostal', models.CharField(blank=True, db_column='codePostal', max_length=25, null=True)),
                ('ville', models.CharField(blank=True, max_length=50, null=True)),
                ('pays', models.CharField(blank=True, max_length=50, null=True)),
                ('sujet', models.CharField(blank=True, max_length=3000, null=True)),
                ('salaire', models.CharField(blank=True, max_length=10, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('ideleve', models.ForeignKey(blank=True, db_column='idEleve', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backoffice.Eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.CharField(blank=True, max_length=100, null=True)),
                ('motdepasse', models.CharField(blank=True, db_column='motDePasse', max_length=50, null=True)),
                ('adresse', models.CharField(blank=True, max_length=100, null=True)),
                ('codepostal', models.CharField(blank=True, db_column='codePostal', max_length=10, null=True)),
                ('ville', models.CharField(blank=True, max_length=100, null=True)),
                ('pays', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accede',
            fields=[
                ('idutilisateur', models.ForeignKey(db_column='idUtilisateur', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backoffice.Utilisateur')),
                ('idfonction', models.ForeignKey(db_column='idFonction', on_delete=django.db.models.deletion.DO_NOTHING, to='backoffice.Fonction')),
            ],
        ),
        migrations.AddField(
            model_name='connexion',
            name='idutilisateur',
            field=models.ForeignKey(blank=True, db_column='idUtilisateur', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backoffice.Utilisateur'),
        ),
    ]
