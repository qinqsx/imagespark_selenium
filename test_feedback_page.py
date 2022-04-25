import pytest
import time
from .pages.base_page import BasePage
from .pages.locators import BasePageLocators


"""Тесты для feedback_page"""

def test_guest_can_see_success_message_with_fill_form_and_upload_file(browser):              #тест, видит ли гость сообщение об успешной отправке формы, при заполненных полях и загруженом файле
    link = BasePageLocators.LINK
    base_page = BasePage(browser, link)
    base_page.open()
    base_page.fill_text_forms(BasePageLocators.NAME_LINK, BasePageLocators.EMAIL_LINK, BasePageLocators.PHONE_LINK, BasePageLocators.MESSAGE_LINK)
    base_page.upload_file_from_current_dir(BasePageLocators.FILE_NAME_LINK)
    base_page.click_submit()
    base_page.should_be_success_message()
