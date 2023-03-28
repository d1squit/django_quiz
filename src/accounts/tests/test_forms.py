from accounts.forms import UserRegisterForm, UserRetryVerification

from django.test import TestCase


class TestForms(TestCase):
    def setUp(self):
        self.username = 'user_1'
        self.password = '123qwe!@#'
        self.email = 'user_1@test.com'

    def test_register_form_no_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_retry_verification_no_data(self):
        form = UserRetryVerification(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
