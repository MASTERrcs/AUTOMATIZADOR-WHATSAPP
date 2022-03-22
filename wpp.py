import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

list = "number1 number2".split()

class Whatsapp:
    def __init__(self):
        self.text = "- Mãe tem café? - Tem não! - Por vou cumer ma aboba com leite AHHVVVSSVGVGAvGGACGAVHAVGAVg!"
        self.user = "SEU NOME DE USUÁRIO WINDOWS"
        options = Options()
        options.add_argument(f"--user-data-dir=C:/Users/{self.user}/AppData/Local/Google/Chrome/User Data")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def Enviar(self, number):
        link = f"https://web.whatsapp.com/send?phone={number}&text={self.text}"
        self.driver.get(f"{link}")
        time.sleep(30)
        send = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
        send.click()
        time.sleep(4)
        self.driver.close()

for number in list:
    try:
        run = Whatsapp()
        run.Enviar(number)
    except Exception as erros:
        run.driver.close()
        print(f"{erros}")
