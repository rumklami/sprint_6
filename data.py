import curl
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class Credentials:
    email = 'ya@asdfsdf.ru'
    password = '1a2b3c'


class Data:
    question = [
        (1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (2,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (3,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (6,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]

    header = [
        (MainPageLocators.SCOOTER, curl.main_page, MainPageLocators.ORDER_BODY),
        (MainPageLocators.YANDEX, curl.yandex_dzen, MainPageLocators.DZEN)
    ]

    orders = [MainPageLocators.ORDER_HEAD, MainPageLocators.ORDER_BODY]
    colours = [OrderPageLocators.BLACK, OrderPageLocators.GREY]
    period = [1, 2, 3, 4, 5, 6, 7]
