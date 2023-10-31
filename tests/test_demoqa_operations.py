from lesson10_hw.pages.registration_page import RegistrationPage
from lesson10_hw.users.user_registration import User, Gender
from datetime import date


def test_registered_user_data():
    student = User(
        first_name='Ivan',
        last_name='Petrov',
        email='petrov@mail.ru',
        genders=[Gender.male.value],
        number='7928777777',
        date_of_birth=date(1999, 8, 9),
        subject='Biology',
        hobbies='Sports',
        picture='ball.jpg',
        address='Russia Moscow',
        state='NCR',
        city='Noida')

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.registered_user_data_should(student)
