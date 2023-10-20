from lesson10_hw.users.user_simple_registration import User
from lesson10_hw.pages.simple_registration_page import SimpleUserRegistrationPage
from dataclasses import dataclass


def test_registers_user():
    admin = User(
        name='Petrov Piter',
        email='pp@moal.com',
        current_address='Russia Moscow',
        permanent_address='Russian Piter'
    )

    simple_registration_page = SimpleUserRegistrationPage()
    simple_registration_page.open()
    simple_registration_page.register(admin)
    simple_registration_page.should_have_submited(admin)
    print(admin.name)
