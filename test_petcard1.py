#pytest -v --driver chrome --driver-path C:\chromedriver\chromedriver.exe
import time



from selenium.webdriver.support.ui import WebDriverWait
def test_1(selenium):
    selenium.implicitly_wait(10)
    selenium.get('http://petfriends.skillfactory.ru/login')

# найти поле "почта" и ввести email
    selenium.find_element_by_id('email').send_keys('okkl@mail.ru')

# найти поле "пароль" и ввести пароль
    selenium.find_element_by_id('pass').send_keys('12375')

# нажимаем на кнопку входа в аккаунт
    selenium.find_element_by_css_selector('button[type="submit"]').click()

#проверяем, что мы оказались на главной странице пользователя
    assert selenium.find_element_by_tag_name('h1').text == "PetFriends"
#проверяем карточки питомцев:

    images = selenium.find_elements_by_css_selector('.card-deck.card-img-top')
    names = selenium.find_elements_by_css_selector('.card-deck.card-title')
    descriptions = selenium.find_elements_by_css_selector('.card-deck.card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0