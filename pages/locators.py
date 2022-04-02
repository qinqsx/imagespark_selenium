from selenium.webdriver.common.by import By

"""Классы с локаторами для страниц и ссылки на них, для улучшения читаемости кода, так же в случае изменения селектора или ссылки на тот или иной объект упрощает корректировку"""

class BasePageLocators():
    NAME_LINK = "Alexey Alexeev"
    EMAIL_LINK = "alexeevam@icloud.com"
    PHONE_LINK = "89992472090"
    MESSAGE_LINK = "test message"
    FILE_NAME_LINK = "file_to_upload.doc"

    LINK = "http://test-form.sibirix.ru/"
    NAME_FORM_LINK = (By.NAME, "name")
    EMAIL_FORM_LINK = (By.NAME, "email")
    PHONE_FORM_LINK = (By.NAME, "phone")
    MESSAGE_FORM_LINK = (By.NAME, "message")
    FILE_UPLOAD_LINK = (By.CSS_SELECTOR, "[type='file']")
    SUBMIT_BUTTON_LINK = (By.CSS_SELECTOR, ".submit")
    SUCCESS_MESSAGE_LINK = (By.CSS_SELECTOR, ".form-wrapper>h1")