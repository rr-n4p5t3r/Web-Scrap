# Web-Scrap - Clics Automaticos
# Desarrollado por Ricardo Rosero - n4p5t3r
# Email: rrosero2000@gmail.com
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Configurar el navegador
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Habilitar el modo headless, para que se ejecute via terminal

# Inicializar el navegador Firefox
driver = webdriver.Firefox(options=options)

# Abrir la página web
url = 'https://www.dian.gov.co/dian/ventasremates/Paginas/Donaciones.aspx'
driver.get(url)

# Realizar clic en todos los elementos con href="#collapse4" utilizando JavaScript
links = driver.find_elements(By.CSS_SELECTOR, '[href="#collapse4"]')
for link in links:
    driver.execute_script("arguments[0].click();", link)

# Realizar clic en todos los elementos con la referencia '/_layouts/15/images/spcommon.png?rev=40' utilizando JavaScript
elements = driver.find_elements(By.CSS_SELECTOR, '[src*="/_layouts/15/images/spcommon.png?rev=40"]')
for element in elements:
    driver.execute_script("arguments[0].click();", element)

# Obtener el contenido HTML de la página
page_content = driver.page_source

# Guardar el contenido en un archivo HTML
with open('./src/pagina_web.html', 'w+', encoding='utf-8') as file:
    file.write(page_content)

# Finalizar la sesión del navegador
driver.quit()
