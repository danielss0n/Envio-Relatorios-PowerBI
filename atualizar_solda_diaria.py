from functions import wait_to_click, save_print, driver; import time

def init():
    driver.get("https://app.powerbi.com/relatorio2")

    wait_to_click("//div[contains(@title, 'SOLDA TOTAL')]"); time.sleep(5)
    save_print("solda diaria", "01 - SOLDA TOTAL")

    wait_to_click("//div[contains(@title, 'AGW 1T')]"); time.sleep(3)
    save_print("solda diaria", "02 - AGW 1T")

    wait_to_click("//div[contains(@title, 'AGW 2T')]"); time.sleep(3)
    save_print("solda diaria", "03 - AGW 2T")

    wait_to_click("//div[contains(@title, 'AGW 3T')]"); time.sleep(3)
    save_print("solda diaria", "05 - AGW 3T")

    wait_to_click("//div[contains(@title, 'AGW GERAL')]"); time.sleep(3)
    save_print("solda diaria", "06 - AGW GERAL")

    wait_to_click("//div[contains(@title, 'CARCAÇAS 1T')]"); time.sleep(3)
    save_print("solda diaria", "07 - CARCAÇAS 1T")

    wait_to_click("//div[contains(@title, 'CARCAÇAS 2T')]"); time.sleep(3)
    save_print("solda diaria", "08 - CARCAÇAS 2T")

    wait_to_click("//div[contains(@title, 'CARCAÇAS 3T')]"); time.sleep(3)
    save_print("solda diaria", "09 - CARCAÇAS 3T")

    wait_to_click("//div[contains(@title, 'CARCAÇAS GERAL')]"); time.sleep(3)
    save_print("solda diaria", "10 - CARCAÇAS GERAL")

    wait_to_click("//div[contains(@title, 'TURBINAS 1T')]"); time.sleep(3)
    save_print("solda diaria", "11 - DIV LEVE 1T")

    wait_to_click("//div[contains(@title, 'TURBINAS 2T')]"); time.sleep(3)
    save_print("solda diaria", "12 - DIV LEVE 2T")

    wait_to_click("//div[contains(@title, 'TURBINAS 3T')]"); time.sleep(3)
    save_print("solda diaria", "13 - DIV LEVE 3T")

    wait_to_click("//div[contains(@title, 'DIV LEVE TOTAL')]"); time.sleep(3)
    save_print("solda diaria", "14 - DIV LEVE TOTAL")

    time.sleep(1)