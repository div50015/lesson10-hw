from selene import browser, have, be, command
import os
from lesson10_hw.users.user_registration import User, Gender
from pathlib import Path


class RegistrationPage:
    def open(self):
        browser.open('/')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.8)"')
        browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(user.date_of_birth.year)
        browser.element('.react-datepicker__month-select').type(user.date_of_birth.strftime('%B'))
        browser.element(f'.react-datepicker__day--00{user.date_of_birth.day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbies)).click()
        browser.element("#uploadPicture").send_keys(os.path.abspath(
            Path(__file__).parent.parent.parent.joinpath(f'tests/files/{user.picture}')))
        browser.element('#currentAddress').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').click()

    def registered_user_data_should(self, user: User):
        user.date_of_birth = f'0{user.date_of_birth.day} {user.date_of_birth.strftime("%B")},{user.date_of_birth.year}'
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.number,
                user.date_of_birth,
                user.subject,
                user.hobbies,
                user.picture,
                user.address,
                f'{user.state} {user.city}',
            )
        )
