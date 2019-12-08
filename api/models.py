from django.db import models


class Address(models.Model):
    country = models.TextField()
    city = models.TextField()
    street = models.TextField()
    building_number = models.IntegerField()
    postal_code = models.IntegerField()
    zip_code = models.IntegerField()

    class Meta:
        db_table = 'address'


class UserInfo(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.TextField()
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='user_info')

    class Meta:
        db_table = 'user_info'


class University(models.Model):
    name = models.TextField()
    rating = models.FloatField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='university')

    class Meta:
        db_table = 'university'


class Student(models.Model):
    student_id_number = models.TextField()
    specialty = models.TextField()
    group = models.TextField()
    semester = models.IntegerField()
    training_form = models.TextField()
    user_info = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='student')
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')

    class Meta:
        db_table = 'student'


class Teacher(models.Model):
    specialty = models.TextField()
    salary = models.IntegerField()
    user_info = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='teacher')
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='teachers')

    class Meta:
        db_table = 'teacher'


class StudentPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_performance')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='student_performance')
    course_name = models.TextField()
    date = models.DateTimeField()
    score = models.IntegerField()

    class Meta:
        db_table = 'student_performance'
