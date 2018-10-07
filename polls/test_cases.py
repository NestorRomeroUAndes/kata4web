__author__ = 'johanna gutierres - nestor romero'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        #self.browser = webdriver.Chrome('E:\\Nestor\\OneDrive\\Documentos\\uniandes\\201820\\procesos agiles\\chromedriver.exe')
        self.browser = webdriver.Chrome('E:\\chromedriver_win32\\chromedriver.exe')
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro_trabajador(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Johanna Marcela')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Gutierrez Meza')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('9')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Ingeniero']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3224624690')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jm.gutierrez@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('E:\\chromedriver_win32\\POL03.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('jm.gutierrez')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('password')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Nombre: Johanna Marcela Apellido: Gutierrez Meza"]')

        self.assertIn('Nombre: Johanna Marcela Apellido: Gutierrez Meza', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Nombre: Johanna Marcela Apellido: Gutierrez Meza"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Johanna Marcela Gutierrez Meza"]')

        self.assertIn('Johanna Marcela Gutierrez Meza', h2.text)

    def test_login2(self):
        self.browser.get('http://localhost:8000')
        link2 = self.browser.find_element_by_id('id_login')
        link2.click()

        usuario2 = self.browser.find_element_by_id('username')
        usuario2.send_keys('jm.gutierrez')

        contrasena2 = self.browser.find_element_by_id('password')
        contrasena2.send_keys('password')

        botonAceptar2 = self.browser.find_element_by_id('aceptar')
        botonAceptar2.click()

        self.browser.implicitly_wait(3)

        span2 = self.browser.find_element(By.XPATH, '//span[text()="Bienvenida Johanna"]')

        self.assertIn('Bienvenida Johanna', span2.text)
