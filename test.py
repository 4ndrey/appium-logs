import unittest
import os
import json
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '13.3' 
		
		desired_caps['deviceName'] = 'iPhone 6s'		
		desired_caps['udid'] = '3125a33178a667ff52e579407ea6bf98bb558bba'

		# desired_caps['deviceName'] = 'iPhone 8 Plus'		
		# desired_caps['udid'] = 'dd3d4e95cbaa34ee80dabe53605d7fc55cd155b8'

		# desired_caps['deviceName'] = 'iPhone XR'		
		# desired_caps['udid'] = '00008020-001410821EF1002E'

		desired_caps["noReset"] = True
		desired_caps['maxTypingFrequency'] = 10000

		desired_caps['simpleIsVisibleCheck'] = True
		desired_caps['useJSONSource'] = True

		desired_caps['showXcodeLog'] = True
		desired_caps['showIOSLog'] = True

		desired_caps["xcodeOrgId"] = '965K7JZC87'
		desired_caps["xcodeSigningId"] = "iPhone Developer"
		desired_caps["bundleId"] = "com.apple.Preferences"
		desired_caps["updatedWDABundleId"] = "com.facebook.WebDriverAgentRunner.check24"

		self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

	def tearDown(self):
		self.driver.quit()

	def editName(self):
		self.driver.find_element_by_name('Name').click()
		field = self.driver.find_element_by_class_name('XCUIElementTypeTextField')
		text = field.text
		field.clear()
		field.set_value(text)
		field.send_keys(Keys.RETURN)
		# self.driver.back()		

	def testOne(self):
		self.driver.find_element_by_name('General').click()
		self.driver.find_element_by_name('About').click()
		for x in range(0, 10):
			self.editName()

if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
        unittest.TextTestRunner(verbosity=2).run(suite)