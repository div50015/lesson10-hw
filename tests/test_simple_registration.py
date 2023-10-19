from lesson10_hw.users.user_simple_registration import User
from lesson10_hw.pages.simple_registration_page import SimpleUserRegistrationPage

admin = User()
admin.name='Petrov Piter'
admin.email='pp@moal.com'
admin.current_address='Russia Moscow'
admin.permanent_address='Russian Piter'


def test_registers_user():
    # admin = User(
    #     name='Petrov Piter',
    #     email='pp@moal.com',
    #     current_address='Russia Moscow',
    #     permanent_address='Russian Piter'
    # )
    simple_registration_page = SimpleUserRegistrationPage()
    simple_registration_page.open()
    simple_registration_page.register(admin)
    print(admin.name)


