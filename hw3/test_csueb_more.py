'''
Sample solution for CS 4320, Spring 2016, revised for Fall 2016
[haven't gotten the search question to work, so skipping that for now]
'''
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from datetime import date

class TestCSUEB(unittest.TestCase):

    def test_footer(self):
        ''' Check content of footer
        '''
        footer_logo = driver.find_element(By.XPATH, '//div[@class="footer-logo col-md-12 text-center"]')
        contact_info = footer_logo.find_element(By.TAG_NAME, "p").text
        self.assertTrue("25800 Carlos Bee Boulevard" in contact_info)
        self.assertTrue("Hayward, CA 94542" in contact_info)
        self.assertTrue("510-885-3000" in contact_info)

        footer = driver.find_element(By.CLASS_NAME, 'copyright')
        copyright_text = footer.text
        # One nice thing about Python 3 is the better support for unicode
        # and special characters, like the copyright character
        self.assertEqual("© %d CALIFORNIA STATE UNIVERSITY, EAST BAY. ALL RIGHTS RESERVED." % date.today().year, copyright_text)

    def test_links(self):
        ''' Check (some of) the links on the home page
            The only test case that still passed after the
            update of the website over the summer of 2016
        '''
        prospective = driver.find_element(By.LINK_TEXT, "Prospective Students")
        prospective.click()
        self.assertEqual("Prospective Students Home Page", driver.title)
        driver.back()
        current = driver.find_element(By.LINK_TEXT, "Current Students")
        current.click()
        self.assertEqual("Current Students at Cal State East Bay", driver.title)
        driver.back()
        current = driver.find_element(By.LINK_TEXT, "Alumni & Friends")
        current.click()
        self.assertEqual("Alumni Association", driver.title)

    def test_quicklinks(self):
        ''' Check the Blackboard link on Quicklinks, assuming it is the top link
        '''
        # Quicklinks is no longer on the home page, so navigate to the Academics page
        academics_link = driver.find_element(By.XPATH, '//div[text()="Academics"]')
        academics_link.click()
        # First get the quicklinks to show
        quicklinks_toggle = driver.find_element(By.ID, "quicklinks-toggle-link")
        quicklinks_toggle.click()
        # Now you can find the element
        quicklinks = driver.find_element(By.ID, "vt_ql_list")
        blackboard = quicklinks.find_element(By.XPATH, "li/a")
        blackboard.click()
        self.assertEqual("Blackboard – Blackboard Learn", driver.title)

    def test_social_icons(self):
        ''' Check that each element of the social slider contains an image element with a JPG source
            (Home page replaced the slide show with a video)
        '''
        # There is at least one other set of slides, so we first find the
        # social networking links component
        social = driver.find_element(By.XPATH, '//div[@class="flexslider social-slider"]')
        slides = social.find_element(By.CLASS_NAME, "slides")
        for slide in slides.find_elements(By.TAG_NAME, "li"):
            # for XPath, if searching from a WebElement like slide,
            # use "." to continue xpath from this element
            image = slide.find_element(By.XPATH, ".//img")
            self.assertEqual(".jpg", image.get_attribute("src")[-4:])
        
    def setUp(self):
        ''' Make sure to go back to the home page before every test case
        '''
        driver.get("http://www.csueastbay.edu/")
                  
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    unittest.main(exit=False) # avoid exiting so we can close the browser
    driver.quit()
