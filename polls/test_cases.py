__author__ = 'johanna gutierres - nestor romero'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('E:\\Nestor\\OneDrive\\Documentos\\uniandes\\201820\\procesos agiles\\chromedriver.exe')
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

