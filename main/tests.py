from django.test import TestCase, Client
from django.urls import reverse
from .models import Student, Notice


class BasicViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Create sample student
        self.student = Student.objects.create(
            full_name="Test Student",
            father_name="Father",
            mother_name="Mother",
            gender="Male",
            address="Test Address",
            city="Test City",
            email="test@student.com",
            contact_num="1234567890",
            date_of_birth="2000-01-01",
            course="BCA",
            stu_id="S101",
            user_name="testuser",
            password="test123"
        )

        # Create public notice
        Notice.objects.create(
            title="Test Notice",
            content="Test Content",
            isPublic=True
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_student_login_success(self):
        response = self.client.post(reverse('student_login'), {
            'userName': 'testuser',
            'stuPwd': 'test123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('student_dashboard'))