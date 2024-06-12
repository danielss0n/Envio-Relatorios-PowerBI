from functions import wait_to_click, save_print, driver; import time

def init():
    driver.get("https://app.powerbi.com/relatorio1") 

    wait_to_click("//div[contains(@title, 'Tendência ID Dept')]"); time.sleep(5)
    save_print("sfm maquinas", "01 - TENDENCIA ID DEPT")

    wait_to_click("//div[contains(@title, 'CALD/MONT Tendência Geral')]"); time.sleep(2)
    save_print("sfm maquinas", "02 - CALD TENDENCIA GERAL")

    wait_to_click("//div[contains(@title, 'Preparação - Tendência ID')]"); time.sleep(2)
    save_print("sfm maquinas", "03 - PREP TENDENCIA GERAN")

    wait_to_click("//div[contains(@title, 'Pacotes - Tendência ID')]"); time.sleep(2)
    save_print("sfm maquinas", "04 - PAC TENDENCIA GERAL")

    wait_to_click("//div[contains(@title, 'Máquinas CALD/MONT')]"); time.sleep(2)
    save_print("sfm maquinas", "05 - CALD MAQUINAS")

    wait_to_click("//div[contains(@title, 'Preparação - Máquinas')]"); time.sleep(2)
    save_print("sfm maquinas", "06 - PREP MAQUINAS")

    wait_to_click("//div[contains(@title, 'Pacotes - Máquinas')]"); time.sleep(2)
    save_print("sfm maquinas", "07 - PAC MAQUINAS")

    wait_to_click("//div[contains(@title, 'Tendência OEE Dept')]"); time.sleep(2)
    save_print("sfm maquinas", "08 - TENDENCIA OEE DEPT")

    wait_to_click("//div[contains(@title, 'CALD/MONT Tendência OEE')]"); time.sleep(2)
    save_print("sfm maquinas", "09 - TENDENCIA OEE CALD")

    wait_to_click("//div[contains(@title, 'Pacotes - Tendência OEE')]"); time.sleep(2)
    save_print("sfm maquinas", "10 - TENDENCIA OEE PAC")

    time.sleep(1)