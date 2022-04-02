from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
import os

"""Инициализация браузера, базовые методы для удобства читаемости и облегчения написания и корректировки кода"""


class BasePage:
    def __init__(self, browser, url, timeout=10):                                       #инициализация браузера, установка времени неявного ожидания
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):                                                                      #переход по ссылке
        self.browser.get(self.url)

    def is_element_present(self, how, what):                                             #представлен ли элемент?
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def element_text(self, how, what):                                                   #текст элемента
        return self.browser.find_element(how, what).text

    def send_text(self, how, what, text):                                                #отправка текста по элементу
        try:
            return self.browser.find_element(how, what).send_keys(text)
        except (NoSuchElementException):
            return NoSuchElementException

    def click_submit(self):                                                              #клик по сабмиту
        try:
            return self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON_LINK).click()
        except (NoSuchElementException):
            return NoSuchElementException

    def upload_file_from_current_dir(self, file):                                              #загрузка файла из директории в которой находится base_page.py
        try:
            current_dir = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(current_dir, file)
            return self.browser.find_element(*BasePageLocators.FILE_UPLOAD_LINK).send_keys(file_path)
        except (NoSuchElementException):
            return NoSuchElementException

    def fill_text_forms(self, name, email, phone, message):                             #заполнение всех форм на странице
        self.send_text(*BasePageLocators.NAME_FORM_LINK, name)
        self.send_text(*BasePageLocators.EMAIL_FORM_LINK, email)
        self.send_text(*BasePageLocators.PHONE_FORM_LINK, phone)
        self.send_text(*BasePageLocators.MESSAGE_FORM_LINK, message)

    def should_be_success_message(self):                                                #ассерт на успешно отправленую заявку
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE_LINK) and self.element_text(*BasePageLocators.SUCCESS_MESSAGE_LINK) == "Сообщение успешно отправлено!", "Success message is not presented"

