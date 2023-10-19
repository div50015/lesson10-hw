from lesson10_hw.users.user_simple_registration import User
from selene import browser


class SimpleUserRegistrationPage:
    def __init__(self):
        self.nameV = browser.element('#userName')
        self.emailV = browser.element('#userEmail')
        self.current_addressV = browser.element('#currentAddress')
        self.permanent_addressV = browser.element('#permanentAddress')
        self.submit_buttonV = browser.element('#submit')

    class locators:
        name = '#userName'
        email = '#userEmail'
        current_address = '#currentAddress'
        permanent_address = '#permanentAddress'
        submit_button = '#submit'

    def open(self):
        browser.open('/')
        return self

    def fill_full_name(self, value):
        self.nameV.type(value)

    def fill_email(self, value):
        self.emailV.type(value)

    def fill_current_address(self, value):
        self.current_addressV.type(value)

    def fill_permanent_address(self, value):
        self.permanent_addressV.type(value)

    def submit(self):
        self.submit_buttonV.click()

    # def should_have_submited(self, full_name, email):
    #     pass

    def register(self, user: User):
        self.fill_full_name(user.name)
        self.fill_email(user.email)
        self.fill_current_address(user.current_address)
        self.fill_permanent_address(user.permanent_address)
        self.submit()
        return self

