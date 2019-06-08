from django.db import models

# Create your models here.


class Account(models.Model):
    user_name = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=64)
    tel = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    user_type = models.CharField(
        max_length=16,
        choices=(('ADMIN', 'ADMIN'), ('PARENT', 'PARENT'), ('ORG', 'ORGANIZATION'), ('TEA', 'TEACHER'))
    )


class Parent(models.Model):
    user_name = models.ForeignKey(Account, primary_key=True, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=64)
    child_birthday = models.DateField()
    child_gender = models.CharField(max_length=16, choices=(('M', 'MALE'), ('F', 'FEMALE')))
    parent_name = models.CharField(max_length=64)
    parent_contact = models.CharField(max_length=64)
    course_field = models.CharField(max_length=64)
    course_cost = models.PositiveIntegerField()
    course_place = models.CharField(max_length=128)


class EduOrg(models.Model):
    user_name = models.ForeignKey(Account, primary_key=True, on_delete=models.CASCADE)
    org_code = models.CharField(max_length=64)
    org_address = models.CharField(max_length=128)
    org_contact = models.CharField(max_length=64)
    org_introduction = models.TextField()
    edu_field = models.CharField(max_length=64)
    edu_age = models.PositiveIntegerField()
    qualified = models.CharField(max_length=16, choices=(('Y', 'YSE'), ('N', 'NO')))


class Teacher(models.Model):
    user_name = models.ForeignKey(Account, primary_key=True, on_delete=models.CASCADE)
    tea_name = models.CharField(max_length=64)
    tea_gender = models.CharField(max_length=16, choices=(('M', 'MALE'), ('F', 'FEMALE')))
    tea_birthday = models.DateField()
    tea_id_number = models.CharField(max_length=64)
    tea_contact = models.CharField(max_length=64)
    tea_introduction = models.TextField()
    edu_field = models.CharField(max_length=64)
    edu_year = models.PositiveIntegerField()
    edu_age = models.PositiveIntegerField()
    qualified = models.CharField(max_length=16, choices=(('Y', 'YSE'), ('N', 'NO')))


class SysAdmin(models.Model):
    user_name = models.ForeignKey(Account, primary_key=True, on_delete=models.CASCADE)
    page_item_count = models.PositiveIntegerField()
