from lesson10_hw.users.user_simple_registration import User
from lesson10_hw.application import app


def test_registers_user():
    admin = User(
        name='Petrov Piter',
        email='mail@mail.ru',
        current_address='Russia Moscow',
        permanent_address='Russian Rostov'
    )

    app.left_panel.open_simple_registration_form()
    app.left_panel.register(admin)
    app.left_panel.should_have_data(admin)
