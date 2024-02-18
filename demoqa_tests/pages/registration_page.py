from selene import browser, have

from demoqa_tests import path_file


class RegistrationPage:
    @staticmethod
    def open():
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")

    @staticmethod
    def fill_full_name(first, last):
        browser.element('#firstName').type(first)
        browser.element('#lastName').type(last)

    @staticmethod
    def fill_date_of_birth(year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    @staticmethod
    def fill_email(value):
        browser.element('#userEmail').type(value)

    @staticmethod
    def fill_gender(value):
        browser.element(f'[for="gender-radio-{value}"]').click()

    @staticmethod
    def fill_mobile(value):
        browser.element('#userNumber').type(value)

    @staticmethod
    def fill_subject(value):
        browser.element('#subjectsInput').type(value).press_enter()

    @staticmethod
    def choose_hobbies(value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    @staticmethod
    def add_photo(value):
        browser.element('[type=file]').set_value(path_file.path(value))

    @staticmethod
    def fill_current_address(value):
        browser.element('#currentAddress').type(value)

    @staticmethod
    def select_state_city(value1, value2):
        browser.element('#react-select-3-input').type(value1).press_enter()
        browser.element('#react-select-4-input').type(value2).press_enter()

    @staticmethod
    def submit():
        browser.element('#submit').press_enter()

    @staticmethod
    def should_registered_user_with(thanks, full_name, email, gender, mobile, birthdate, subjects, hobbies,
                                    picture, cur_address, state_city):
        browser.element('#example-modal-sizes-title-lg').should(have.text(thanks))
        browser.element('.table-responsive').all('tr>td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            mobile,
            birthdate,
            subjects,
            hobbies,
            picture,
            cur_address,
            state_city))
