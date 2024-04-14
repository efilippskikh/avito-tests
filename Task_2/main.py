from playwright.sync_api import sync_playwright

# Тест 1. Общий скриншот
def test_1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        eco_impact_selector = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div"
        page.query_selector(eco_impact_selector).screenshot(path="./output/1.png")

        browser.close()

# Тест 2. Скриншот счетчика сохранённого объёма воды
def test_2():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        eco_impact_selector = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(4)"
        page.query_selector(eco_impact_selector).screenshot(path="./output/2.png")

        browser.close()


# Тест 3. Скриншот счетчика предотвращённого объёма выброса CO2
def test_3():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        eco_impact_selector = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(2)"
        page.query_selector(eco_impact_selector).screenshot(path="./output/3.png")

        browser.close()

# Тест 4. Скриншот счетчика сэкономленной электроэнергии
def test_4():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        eco_impact_selector = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(6)"
        page.query_selector(eco_impact_selector).screenshot(path="./output/4.png")

        browser.close()

# Тест 5. Скриншот аватара пользователя
def test_5():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        eco_impact_selector = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(5)"
        page.query_selector(eco_impact_selector).screenshot(path="./output/5.png")

        browser.close()


