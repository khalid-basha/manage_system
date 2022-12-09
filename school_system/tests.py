from django.test import TestCase
from .models import User, Teacher, Course, Student
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager
import json
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth import authenticate

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username="testuser1",
            user_type=1,
            password = "testpass1",
            mobile_num="+923331234567",
            birth_date="1999-09-09"
        )
        User.objects.create(
            username="testuser2",
            user_type=2,
            mobile_num="+923331234568",
            birth_date="1999-09-09"
        )
        User.objects.create(
            username="testuser3",
            user_type=3,
            mobile_num="+923331234569",
            birth_date="1999-09-09"
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 3)

    def test_user_fields(self):
        user = User.objects.get(username="testuser1")
        self.assertEqual(user.username, "testuser1")
        self.assertEqual(user.password, "testpass1")
        self.assertEqual(user.user_type, 1)
        self.assertEqual(user.mobile_num, "+923331234567")
        self.assertEqual(user.birth_date.strftime("%Y-%m-%d"), "1999-09-09")

    def test_user_manager(self):
        self.assertIsInstance(User.objects, UserManager)

    def test_user_string_representation(self):
        user = User.objects.get(username="testuser1")
        self.assertEqual(str(user), "testuser1")

    def test_user_type_admin(self):
        testuser1 = User.objects.get(username="testuser1")
        self.assertEqual(testuser1.user_type, 1)

    def test_user_type_student(self):
        testuser2 = User.objects.get(username="testuser2")
        self.assertEqual(testuser2.user_type, 2)

    def test_user_type_teacher(self):
        testuser3 = User.objects.get(username="testuser3")
        self.assertEqual(testuser3.user_type, 3)

    def test_user_created_student(self):
        testuser2 = User.objects.get(username="testuser2")
        user = Student.objects.get(pk=testuser2.id)
        self.assertTrue(isinstance(user, Student))

    def test_user_created_teacher(self):
        testuser3 = User.objects.get(username="testuser3")
        user = Teacher.objects.get(pk=testuser3.id)
        self.assertTrue(isinstance(user, Teacher))

class TeacherTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
            user_type=3,
            mobile_num="+923331234558",
            birth_date="1999-09-09"

        )

    def test_teacher_created(self):
        user =User.objects.get(username="test_user")
        teacher = Teacher.objects.get(pk=user.id)
        self.assertEqual(teacher.user.username, 'test_user')

    def test_teacher_courses(self):
        user =User.objects.get(username="test_user")
        teacher = Teacher.objects.get(pk=user.id)
        course1 = Course.objects.create(
            title='Test Course 1',
            subject='Test Subject 1',
            hours=20,
            teacher=teacher
        )
        course2 = Course.objects.create(
            title='Test Course 2',
            subject='Test Subject 2',
            hours=30,
            teacher=teacher
        )

        self.assertQuerysetEqual(teacher.course_set.all(),
            {course1, course2},
            ordered=False
        )

class StudentTestCase(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
            user_type=2
        )

    def test_student_created(self):
        student = Student.objects.get(user__username='test_user')
        self.assertEqual(student.user.username, 'test_user')

    def test_student_courses(self):
        student = Student.objects.get(user__username='test_user')
        course1 = Course.objects.create(
            title='Test Course 1',
            subject='Test Subject 1',
            hours=20
        )
        course2 = Course.objects.create(
            title='Test Course 2',
            subject='Test Subject 2',
            hours=30
        )
        student.courses.add(course1, course2)
        self.assertQuerysetEqual(student.courses.all(),
            {course1, course2},
            ordered=False
        )
class CourseTestCase(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
                        user_type=3
        )
        teacher = Teacher.objects.get(pk=user.id)
        Course.objects.create(
            title='Test Course',
            subject='Test Subject',
            hours=20,
            teacher=teacher
        )

    def test_course_created(self):
        course = Course.objects.get(title='Test Course')
        self.assertEqual(course.title, 'Test Course')
        self.assertEqual(course.subject, 'Test Subject')
        self.assertEqual(course.hours, 20)
        self.assertEqual(course.teacher.user.username, 'test_user')

    def test_course_students(self):
        course = Course.objects.get(title='Test Course')
        user1 = get_user_model().objects.create_user(
            username='test_user1',
            password='test_password1',
            user_type=2
        )
        user2 = get_user_model().objects.create_user(
            username='test_user2',
            password='test_password2',
            user_type=2
        )
        student1 = Student.objects.get(user=user1)
        student2 = Student.objects.get(user=user2)
        student1.courses.add(course)
        student2.courses.add(course)

        self.assertQuerysetEqual(course.enrolled_students.all(),
            [student1, student2],
            ordered=False
        )



class ViewsTestCase(TestCase):
    def setUp(self):

        self.client=Client()

        self.user1 = get_user_model().objects.create(username="user1",
                password = "user1",user_type=1,mobile_num="+923331234567",
                birth_date="1999-09-09")
        self.user2 = get_user_model().objects.create(username="user2",
                password='user2',user_type=2,mobile_num="+923331234568",
                birth_date="1999-09-09")
        self.user3 = get_user_model().objects.create(username='user3',
                 user_type=3,mobile_num="+923331234569",
                birth_date="1999-09-09")
        self.user3.set_password('user3')
        self.user3.save()
        self.course1 = Course.objects.create(title='Course 1',
                subject='Subject 1', hours=20, teacher_id=self.user3.id)
        self.course2 = Course.objects.create(title='Course 2',
                subject='Subject 2', hours=30, teacher_id=self.user3.id)
        self.student = Student.objects.get(user=self.user2)
        self.student.courses.add(self.course1)

    def test_register(self):
        data = {'username': 'user4', 'password': 'user4', 'user_type': 1}
        response = self.client.post('/register/', json.dumps(data),
                content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_register_with_invalid_data(self):
        data = {'username': 'user4'}
        response = self.client.post('/register/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid data'})

    def test_courses_list(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
         [{"title": "Course 1", "subject": "Subject 1", "hours": 20, 'teacher_id':self.user3.id},
         {"title": "Course 2", "subject": "Subject 2", "hours": 30, 'teacher_id':self.user3.id}])
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            [{"title": "Course 1", "subject": "Subject 1", "hours": 20, 'teacher_id':self.user3.id},
            {"title": "Course 2", "subject": "Subject 2", "hours": 30, 'teacher_id':self.user3.id}])

    def test_teacher_my_courses(self):
        credentials = { 'username': 'user3','password': 'user3'}
        user = authenticate(**credentials)
        self.client._login(user)
        response = self.client.get('/my_courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
         [{"title": "Course 1", "subject": "Subject 1", "hours": 20, 'teacher_id':self.user3.id},
         {"title": "Course 2", "subject": "Subject 2", "hours": 30, 'teacher_id':self.user3.id}])
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/my_courses/')
        self.assertEqual(response.status_code, 302)
