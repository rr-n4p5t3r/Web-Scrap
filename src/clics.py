from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configurar el navegador
options = webdriver.FirefoxOptions()

# Inicializar el navegador Firefox
driver = webdriver.Firefox(options=options)

# Abrir la página web
url = 'https://www.dian.gov.co/dian/ventasremates/Paginas/Donaciones.aspx'
driver.get(url)

# Esperar a que se cargue la página
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'collapse4')))  

for link in driver.find_elements(By.CSS_SELECTOR, '[href="#collapse4"]'):
    link.click()

# Obtener el contenido HTML de la página
page_content = driver.page_source

# Guardar el contenido en un archivo HTML
with open('pagina_web.html', 'w', encoding='utf-8') as file:
    file.write(page_content)

driver.execute_script("javascript:ExpCollGroup('collapse4', 'img_collapse4',event, false);return false;")
driver.execute_script("javascript:ExpCollGroup('collapse5', 'img_collapse5',event, false);return false;")
driver.execute_script("javascript:ExpCollGroup('scriptWPQ5', 'img_scriptWPQ5',event, false);return false;")


# Finalizar la sesión del navegador
driver.quit()
