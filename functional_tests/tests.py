from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class RegisterTest(LiveServerTestCase):
    chrome_driver_location = os.path.dirname(os.path.abspath(__file__))+"\\chromedriver.exe"

    def setUp(self):
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
