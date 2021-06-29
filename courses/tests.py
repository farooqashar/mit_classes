from django.test import TestCase
from .models import *

# Create your tests here.

class ClassModelTests(TestCase):

    def test_course_6_class(self):
        course_18_class = Class(class_name="18.600")
        self.assertIs(course_18_class.is_course_6(), False)

    def test_course_6_class1(self):
        course_8_class = Class(class_name="8.02")
        self.assertIs(course_8_class.is_course_6(), False)

    def test_course_6_class2(self):
        course_6_class = Class(class_name="6.009")
        self.assertIs(course_6_class.is_course_6(), True)