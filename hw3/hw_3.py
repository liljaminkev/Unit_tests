import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import itertools

class TestMonterrayBayAquarium(unittest.TestCase):
#check physical address on page
    def testPhysicalAddress(self):
        #get footer
        siteFooter = driver.find_element(By.XPATH, '/html/body/footer/div[@class="container"]/div[@class="row"]/div[@class="item"]/span[@class="footer"]')
        #get address elements
        streetAddress = siteFooter.find_element_by_xpath("//span[@itemprop = 'streetAddress']").text
        addressLocal = siteFooter.find_element_by_xpath("//span[@itemprop ='addressLocality']").text
        addressRegion = siteFooter.find_element_by_xpath("//span[@itemprop = 'addressRegion']").text
        postalCode = siteFooter.find_element_by_xpath("//span[@itemprop = 'postalCode']").text
        
        #test all at once
        self.assertTrue("886 Cannery Row" == streetAddress and "Monterey" == addressLocal and "CA" == addressRegion and "93940" == postalCode)
        
        #test elements seperately if wanted
        #self.assertTrue("Monterey" == addressLocal)
        #self.assertTrue("CA" == addressRegion)
        #self.assertTrue("93940" == postalCode)

#check that conservation link works and heading is right
    def testConservationPage(self):
        siteNav = driver.find_element_by_class_name('site-nav')
        conservationLink = siteNav.find_element_by_partial_link_text('Conserva')
        conservationLink.click()
        heading = driver.find_element_by_class_name('page-title').text
        
        self.assertTrue("Conservation & Science" == heading)
        
        links = driver.find_element_by_xpath('/html/body/main/div[@class="container"]/div[@class="page"]/div[@class="content"]/div[@class="group group-of-verticals items-3"]')
        
        #test link 1
        link = links.find_element_by_xpath('//a[@href = "/conservation-and-science/our-priorities/california-ocean-health"]/div[@class = "item-inner"]/div[@class="item-content"]').text
        self.assertTrue("California Ocean Health" == link)
        
        #test link 2
        link = links.find_element_by_xpath('//a[@href = "/conservation-and-science/our-priorities/thriving-ocean-wildlife"]/div[@class = "item-inner"]/div[@class="item-content"]').text
        self.assertTrue("Thriving Ocean Wildlife" == link)
        
        #test link 3
        link = links.find_element_by_xpath('//a[@href = "/conservation-and-science/our-priorities/sustainable-fisheries-and-aquaculture"]/div[@class = "item-inner"]/div[@class="item-content"]').text
        self.assertTrue("Sustainable Fisheries & Aquaculture" == link)

    def setUp(self):
        driver.get("https://www.montereybayaquarium.org") #set main webpage 
    
class TestSeaFoodWatch(unittest.TestCase):
#test a failing string
    def testNoStringFound(self):
        search = driver.find_element_by_xpath('//input[@class = "typeahead tt-input"]')
        search.send_keys("blahblah")
        search.send_keys(Keys.RETURN)
    
        text = driver.find_element_by_xpath('//div[@ng-hide = "model.groups"]').text
        self.assertTrue("No matches found" in text)
#test a green badge only string
    def testSearchGreen(self):
        search = driver.find_element_by_xpath('//input[@class = "typeahead tt-input"]')
        search.send_keys("lionfish")
        search.send_keys(Keys.RETURN)
        driver.find_element_by_xpath('//a[@class = "button centered ng-binding"]').click() #currently goes to overview page
        driver.find_element_by_class_name('filter-ratings')
        
        greyBadge = driver.find_element_by_xpath('//a[@class="grey badge ng-hide"]').text
        self.assertTrue("" == greyBadge)
        
        redBadge = driver.find_element_by_xpath('//a[@class="red badge ng-hide"]').text
        self.assertTrue("" == redBadge)
        
        yellowBadge = driver.find_element_by_xpath('//a[@class="yellow badge ng-hide"]').text
        self.assertTrue("" == yellowBadge)
        
        greenBadge = driver.find_element_by_xpath('//a[@class="green badge"]').text
        self.assertTrue("4" in greenBadge)

#test yellow only string
    def testSearchYellow(self):
        search = driver.find_element_by_xpath('//input[@class = "typeahead tt-input"]')
        search.send_keys("Grenadier")
        search.send_keys(Keys.RETURN)
        driver.find_element_by_xpath('//a[@class = "button centered ng-binding"]').click() #currently goes to overview page
        driver.find_element_by_class_name('filter-ratings')
        
        greyBadge = driver.find_element_by_xpath('//a[@class="grey badge ng-hide"]').text
        self.assertTrue("" == greyBadge)
        
        redBadge = driver.find_element_by_xpath('//a[@class="red badge ng-hide"]').text
        self.assertTrue("" == redBadge)
        
        yellowBadge = driver.find_element_by_xpath('//a[@class="yellow badge"]').text
        self.assertTrue("3" in yellowBadge) # has 3 at time of search
        
        greenBadge = driver.find_element_by_xpath('//a[@class="green badge ng-hide"]').text
        self.assertTrue("" == greenBadge)
    
    def setUp(self):
        driver.get("http://www.seafoodwatch.org") #set main webpage

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    unittest.main(exit=False) # avoid exiting so we can close the browser
    driver.quit()
