from django.test import LiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
import time
import os


class RegistrationTest(LiveServerTestCase):
    chrome_driver_location = os.path.dirname(os.path.abspath(__file__))+"\\chromedriver.exe"

    def setUp(self):
        # For Firefox see: http://stackoverflow.com/a/37728659
        # Use Chrome for now
        self.browser = webdriver.Chrome(self.chrome_driver_location)
        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_register_title(self):
        self.browser.get(self.live_server_url+'/accounts/register/')
        title_text = 'Register'
        self.assertIn(title_text, self.browser.title)

    def test_user_can_create_account(self):
        # A user navigates to /accounts/register
        self.browser.get(self.live_server_url + '/accounts/register/')

        # They are shown a form in which they can enter username, email and password
        page_html = self.browser.page_source
        self.assertIn('id_username', page_html)
        self.assertIn('id_email', page_html)
        self.assertIn('id_password', page_html)
        self.assertIn('id_submit', page_html)

        # The user enters their data and submits the form
        username_input = self.browser.find_element_by_id('id_username')
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        submit_button = self.browser.find_element_by_id('id_submit')
        username_input.send_keys('test')
        email_input.send_keys('test@test.test')
        password_input.send_keys('testtest')
        submit_button.click()

        # And they are redirected to the home page.
        self.assertEqual(self.live_server_url + '/', self.browser.current_url)

    def test_user_can_login(self):
        ## Create the user before loging in
        User.objects.create_user(username='test', email='test@test.test', password='testtest')

        logout_link = self.live_server_url + '/accounts/logout/'
        login_link = self.live_server_url + '/accounts/login/'

        # The user navigates to /accounts/login
        self.browser.get(login_link)

        # Show login form
        page_html = self.browser.page_source
        self.assertIn('id_username', page_html)
        self.assertIn('id_password', page_html)
        self.assertIn('id_submit', page_html)

        # The user enters login information username, password.
        # Then click submit.
        username_input = self.browser.find_element_by_id('id_username')
        password_input = self.browser.find_element_by_id('id_password')
        submit_button = self.browser.find_element_by_id('id_submit')
        username_input.send_keys('test')
        password_input.send_keys('testtest')
        submit_button.click()

        # Redirect to home page.
        self.assertEqual(self.live_server_url + '/', self.browser.current_url)

        # In the end the user logs out
        # And is redirected to the login page
        self.browser.get(logout_link)
        self.assertEqual(login_link, self.browser.current_url)



