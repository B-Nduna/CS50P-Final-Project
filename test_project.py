import unittest
from unittest.mock import patch
from project import get_personal_details, get_education_details, get_work_experience, get_skills

class TestResumeBuilder(unittest.TestCase):

    @patch('builtins.input', side_effect=['John Doe', 'johndoe@email.com', '1234567890', 'Software Engineer'])
    def test_get_personal_details(self, mock_input):
        expected_output = {'name': 'John Doe', 'email': 'johndoe@email.com', 'phone': '1234567890', 'summary': 'Software Engineer'}
        self.assertEqual(get_personal_details(), expected_output)

    @patch('builtins.input', side_effect=['BSc Computer Science', 'ABC University', '2022', 'no'])
    def test_get_education_details(self, mock_input):
        expected_output = [{'degree': 'BSc Computer Science', 'institution': 'ABC University', 'graduation_year': '2022'}]
        self.assertEqual(get_education_details(), expected_output)

    @patch('builtins.input', side_effect=['Tech Company', 'Software Developer', 'Backend Development', 'no'])
    def test_get_work_experience(self, mock_input):
        expected_output = [{'company': 'Tech Company', 'job_title': 'Software Developer', 'role': 'Backend Development'}]
        self.assertEqual(get_work_experience(), expected_output)

    @patch('builtins.input', return_value='Python, Java, SQL')
    def test_get_skills(self, mock_input):
        expected_output = ['Python', 'Java', 'SQL']
        self.assertEqual(get_skills(), expected_output)

if __name__ == '__main__':
    unittest.main()
