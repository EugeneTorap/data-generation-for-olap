import random
import string
from faker import Faker

from api.models import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

RANGE = 1500
UNIVERSITY_RANGE = 110

UNIVERSITY_RANGE2 = 300
USER_INFO_RANGE = 900

UNIVERSITY_NAMES = [
    'University of Pennsylvania', 'Stanford University', 'Harvard University', 'Massachusetts Institute of Technology',
    'University of Chicago', 'Columbia University', 'Northwestern University', 'University of California--Berkeley',
    'Yale University', 'Duke University', 'University of Michigan--Ann Arbor', 'Dartmouth College',
    'New York University', 'University of Virginia', 'Cornell University', 'University of California--Los Angeles',
    'Carnegie Mellon University', 'University of Southern California', 'University of North Carolina--Chapel Hill',
    'University of Texas--Austin', 'Emory University', 'Indiana University', 'University of Washington',
    'Georgetown University', 'University of Florida', 'Rice University', 'University of Notre Dame',
    'Washington University in St. Louis', 'Georgia Institute of Technology', 'Vanderbilt University',
    'Ohio State University', 'Brigham Young University', 'Arizona State University', 'Pennsylvania State University--University Park'
]

SPECIALTY_NAMES = [
    'Accounting', 'Entrepreneurship', 'Executive MBA', 'Finance', 'Marketing', 'Environmental Law', 'Intellectual',
    'Property Law', 'Part-time Law', 'Tax Law', 'Trial Advocacy', 'Anesthesiology', 'Family Medicine',
    'Obstetrics and Gynecology', 'Internal Medicine', 'Pediatrics', 'Surgery', 'Chemical Engineering',
    'Civil Engineering', 'Computer Engineering', 'Environmental / Environmental Health Engineering',
    'Mechanical Engineering', 'Clinical Nurse Leader', 'Nurse Practitioner: Family',
    'Nurse Practitioner: Pediatric, Primary Care', 'Nursing Administration', 'Nursing Informatics'
]

GROUP_NAMES = [
    'First', 'Second', 'Third', 'Fourth'
]

TRAINING_FORM_NAMES = [
    'Day form', 'Extramural form', 'Evening form', 'Distance form'
]

COURSE_NAMES = [
    'Accounting & Finance', 'Aeronautical & Manufacturing Engineering', 'Agriculture & Forestry', 'American Studies',
    'Anatomy & Physiology', 'Anthropology', 'Archaeology', 'Architecture', 'Art & Design', 'Aural & Oral Sciences',
    'Biological Sciences', 'Building', 'Business & Management Studies', 'Celtic Studies', 'Chemical Engineering',
    'Chemistry', 'Civil Engineering', 'Classics & Ancient History', 'Communication & Media Studies',
    'Complementary Medicine', 'Computer Science', 'Counselling', 'Creative Writing', 'Criminology',
    'Dentistry', 'Drama, Dance & Cinematics', 'East & South Asian Studies', 'Economics', 'Education',
    'Electrical & Electronic Engineering', 'English', 'Fashion', 'Film Making', 'Food Science',
    'Forensic Science', 'French', 'Geography & Environmental Sciences', 'Geology', 'General Engineering',
    'German', 'History', 'History of Art, Architecture & Design', 'Hospitality, Leisure, Recreation & Tourism',
    'Iberian Languages/Hispanic Studies', 'Italian', 'Land & Property Management', 'Law',
    'Librarianship & Information Management', 'Linguistics', 'Marketing', 'Materials Technology', 'Mathematics',
    'Mechanical Engineering', 'Medical Technology', 'Medicine', 'Middle Eastern & African Studies',
    'Music', 'Nursing', 'Occupational Therapy', 'Optometry, Ophthalmology & Orthoptics', 'Pharmacology & Pharmacy',
    'Philosophy', 'Physics and Astronomy', 'Physiotherapy', 'Politics', 'Psychology', 'Robotics',
    'Russian & East European Languages', 'Social Policy', 'Social Work', 'Sociology', 'Sports Science',
    'Theology & Religious Studies', 'Town & Country Planning and Landscape Design', 'Veterinary Medicine', 'Youth Work'
]


class RecipeView(viewsets.ViewSet):
    queryset = Address.objects.all()

    @action(detail=False)
    def get(self, request, pk=None):
        faker = Faker()

        address_list = []
        for i in range(RANGE):
            address_list.append(Address(country=faker.country(), city=faker.city(), street=faker.street_name(),
                                        building_number=faker.building_number(), postal_code=faker.postalcode(),
                                        zip_code=faker.zipcode()))
            print('Address')

        Address.objects.bulk_create(address_list)

        user_info_list = []
        for i in range(USER_INFO_RANGE):
            user_info_list.append(UserInfo(first_name=faker.first_name(), last_name=faker.last_name(),
                                           phone=faker.phone_number(), age=random.randint(18, 54), address_id=i+1))
            print('UserInfo')

        UserInfo.objects.bulk_create(user_info_list)

        universities = []
        for i in range(UNIVERSITY_RANGE):
            universities.append(University(name=random.choice(UNIVERSITY_NAMES), rating=random.uniform(1, 99),
                                           address_id=i+6))
            print('University')

        University.objects.bulk_create(universities)

        students = []
        counter = 0
        student_counter = 1
        for i in range(USER_INFO_RANGE):
            counter = counter + 1

            if counter % 90 == 0:
                student_counter = student_counter + 1

            letters_and_digits = string.ascii_letters + string.digits
            id_number = ''.join(random.choice(letters_and_digits) for i in range(18))

            students.append(Student(student_id_number=id_number, specialty=random.choice(SPECIALTY_NAMES),
                                    group=random.choice(GROUP_NAMES), semester=random.randint(1, 10),
                                    training_form=random.choice(TRAINING_FORM_NAMES), user_info_id=i+1,
                                    university_id=student_counter))
            print('Student')

        Student.objects.bulk_create(students)

        teachers = []
        counter = 0
        teacher_counter = 1
        for i in range(UNIVERSITY_RANGE2):
            counter = counter + 1

            if counter % 70 == 0:
                teacher_counter = teacher_counter + 1

            teachers.append(Teacher(specialty=random.choice(SPECIALTY_NAMES), salary=random.randrange(500, 5500, 100),
                                    user_info_id=i+600, university_id=teacher_counter))
            print('Teacher')

        Teacher.objects.bulk_create(teachers)

        student_performances = []
        counter = 0
        student_counter = 1
        teacher_counter = 1
        for i in range(RANGE):
            counter = counter + 1

            if counter % 2 == 0:
                student_counter = student_counter + 1

            if counter % 11 == 0:
                teacher_counter = teacher_counter + 1

            exam_date = faker.date_time_between(start_date="-10y", end_date="now", tzinfo=None)
            student_performances.append(StudentPerformance(course_name=random.choice(COURSE_NAMES), date=exam_date,
                                                           score=random.randint(1, 10), student_id=student_counter,
                                                           teacher_id=teacher_counter))
            print('StudentPerformance')

        StudentPerformance.objects.bulk_create(student_performances)

        return Response(True)
