from lesson10_hw.users.user_simple_registration import User
from selene import browser, be, have


class LeftPanel:
    def __init__(self):
        self.enter_full_name = browser.element('#userName')
        self.enter_email = browser.element('#userEmail')
        self.enter_current_address = browser.element('#currentAddress')
        self.enter_permanent_address = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

        self.check_full_name = browser.element('p#name.mb-1')
        self.check_email = browser.element('p#email.mb-1')
        self.check_current_address = browser.element('p#currentAddress.mb-1')
        self.check_permanent_address = browser.element('p#permanentAddress.mb-1')

        self.open_simple_registration_form = self.open

    def open(self):
        browser.open('/')
        return self

    def should_have_data(self, user: User):
        self.check_full_name.should(have.exact_text(f'Name:{user.name}'))
        self.check_email.should(have.exact_text(f'Email:{user.email}'))
        self.check_current_address.should(have.exact_text(f'Current Address :{user.current_address}'))
        self.check_permanent_address.should(have.exact_text(f'Permananet Address :{user.permanent_address}'))

    def register(self, user: User):
        self.enter_full_name.type(user.name)
        self.enter_email.type(user.email)
        self.enter_current_address.type(user.current_address)
        self.enter_permanent_address.type(user.permanent_address)
        self.submit_button.click()
        return self
