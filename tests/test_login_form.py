import time

from selenium.webdriver import Keys

from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    time.sleep(2)
    # form_page.btn_submit.click_force()
    # time.sleep(2)
    form_page.user_email.send_keys(Keys.CONTROL + 'a')
    time.sleep(2)
    form_page.user_email.send_keys(Keys.DELETE)

    # assert form_page.modal_dialog.exist()
    # time.sleep(2)
    # form_page.btn_close_modal.click_force()





