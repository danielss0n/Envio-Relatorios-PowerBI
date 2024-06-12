from functions import wait_to_click, save_print, driver; import time

def init():
    driver.get("https://app.powerbi.com/relatorio3")
    
    wait_to_click("//div[contains(@title, '1T AGW')]"); time.sleep(5)
    save_print("soldadores", "01 - 1T AGW")

    wait_to_click("//div[contains(@title, '2T AGW')]"); time.sleep(2)
    save_print("soldadores", "02 - 2T AGW")

    wait_to_click("//div[contains(@title, '3T AGW')]"); time.sleep(2)
    save_print("soldadores", "03 - 3T AGW")

    wait_to_click("//div[contains(@title, '1T Carcaça')]"); time.sleep(2)
    save_print("soldadores", "04 - 1T CARCAÇAS")

    wait_to_click("//div[contains(@title, '2T Carcaça')]"); time.sleep(2)
    save_print("soldadores", "05 - 2T CARCAÇAS")

    wait_to_click("//div[contains(@title, '3T Carcaça')]"); time.sleep(2)
    save_print("soldadores", "06 - 3T CARCAÇAS")

    wait_to_click("//div[contains(@title, '1T Turbinas')]"); time.sleep(2)
    save_print("soldadores", "07 - 1T TURBINAS")

    wait_to_click("//div[contains(@title, '2T Turbinas')]"); time.sleep(2)
    save_print("soldadores", "08 - 2T TURBINAS")

    wait_to_click("//div[contains(@title, '3T Turbinas')]"); time.sleep(2)
    save_print("soldadores", "09 - 3T TURBINAS")

    wait_to_click("//div[contains(@title, 'Média Diária/Semanal')]"); time.sleep(2)
    save_print("soldadores", "10 - MEDIA SEMANAL")

    time.sleep(1)