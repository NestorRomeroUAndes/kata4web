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
        nombre.send_keys('Nestor Sebastian')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Romero')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('9')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Ingeniero']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('ns.romerob@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('E:\\chromedriver_win32\\POL03.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('ns.romerob')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('password')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Nombre: Nestor Sebastian Apellido: Romero"]')

        self.assertIn('Nombre: Nestor Sebastian Apellido: Romero', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Nombre: Nestor Sebastian Apellido: Romero"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Nestor Sebastian Romero"]')

        self.assertIn('Nestor Sebastian Romero', h2.text)