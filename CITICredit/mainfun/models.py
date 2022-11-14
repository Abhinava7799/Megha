from django.db import models

# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bankcarddetails(models.Model):
    accountnumber = models.IntegerField(primary_key=True)
    customername = models.CharField(max_length=30, blank=True, null=True)
    bankname = models.CharField(max_length=33, blank=True, null=True)
    cardtypecode = models.CharField(max_length=10, blank=True, null=True)
    cardtypename = models.CharField(max_length=100, blank=True, null=True)
    cardlimit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bankcarddetails'


class Customer(models.Model):
    accountnumber = models.IntegerField(primary_key=True)
    customername = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Department(models.Model):
    # Field name made lowercase.
    deptcode = models.IntegerField(db_column='DEPTCODE', primary_key=True)
    # Field name made lowercase.
    job = models.CharField(
        db_column='Job', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    location = models.CharField(
        db_column='LOCATION', max_length=33, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    # Field name made lowercase.
    empcode = models.IntegerField(
        db_column='EmpCode', primary_key=True)
    # Field name made lowercase.
    empfname = models.CharField(
        db_column='EmpFName', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    emplname = models.CharField(
        db_column='EmpLName', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    job = models.CharField(
        db_column='Job', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    manager = models.CharField(
        db_column='Manager', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)
    # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)
    # Field name made lowercase.
    commission = models.IntegerField(
        db_column='Commission', blank=True, null=True)
    # Field name made lowercase.
    deptcode = models.IntegerField(db_column='DEPTCODE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'
