# Generated by Django 2.0.13 on 2022-11-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankcarddetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnumber', models.IntegerField(blank=True, null=True)),
                ('customername', models.CharField(blank=True, max_length=30, null=True)),
                ('bankname', models.CharField(blank=True, max_length=33, null=True)),
                ('cardtypecode', models.CharField(blank=True, max_length=10, null=True)),
                ('cardtypename', models.CharField(blank=True, max_length=100, null=True)),
                ('cardlimit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bankcarddetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnumber', models.IntegerField(blank=True, null=True)),
                ('customername', models.CharField(blank=True, max_length=30, null=True)),
                ('branch', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptcode', models.IntegerField(blank=True, db_column='DEPTCODE', null=True)),
                ('job', models.CharField(blank=True, db_column='Job', max_length=30, null=True)),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=33, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.IntegerField(blank=True, db_column='EmpCode', null=True)),
                ('empfname', models.CharField(blank=True, db_column='EmpFName', max_length=15, null=True)),
                ('emplname', models.CharField(blank=True, db_column='EmpLName', max_length=15, null=True)),
                ('job', models.CharField(blank=True, db_column='Job', max_length=45, null=True)),
                ('manager', models.CharField(blank=True, db_column='Manager', max_length=4, null=True)),
                ('hiredate', models.DateField(blank=True, db_column='HireDate', null=True)),
                ('salary', models.IntegerField(blank=True, db_column='Salary', null=True)),
                ('commission', models.IntegerField(blank=True, db_column='Commission', null=True)),
                ('deptcode', models.IntegerField(blank=True, db_column='DEPTCODE', null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
    ]
