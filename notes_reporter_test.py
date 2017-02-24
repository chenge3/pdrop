'''
Uses unittest framework and Selenium for testing RESTful API of notes_reporter.

BEFORE THE TEST:
1.  A static copy of the page generated by 800notes.com website has to be used.
    The copy is located at 'http://khaimovich.name/test_page_1.html'. This URL
    has to be assigned to PHONE_SITE constant on the top of scarper.py module.
2.  Selenium Webdriver has to be installed together with the browser specific
    driver (chromedriver is currently being used).
3.  The follwing line has to be changed accordingly:
    <self.driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)>
4.  The PATH_TO_CHROMEDRIVER constant has to point to the location
    of chromedriver.exe.
5.  The file with expected source code good_source_2_results.txt has
    to be placed in the same directory as notes_reporter_test.py.
6.  notes_reporter has to be started on the same system where testing
    is performed.

TO RUN THE TEST:
<python notes_reporter_test.py -v>

READING TEST RESULTS:
The results will be displayed in the console used to run this test.

Here is a good explanation of interpreting the results:
http://www.diveintopython3.net/unit-testing.html

Here is an example of successful completion:

C:\python>python notes_reporter_test.py -v
test_page_content (__main__.TestNotesReporterAPI)
Assert that correct source is generated for the given API command. ... ok

----------------------------------------------------------------------
Ran 1 test in 8.286s

OK
'''
import unittest
from selenium import webdriver

# test parameters
PATH_TO_CHROMEDRIVER = 'C:\\Users\\Leon\\AppData\\Local\\Programs' + \
    '\\Python\\Python35\\Lib\\site-packages\\selenium\\chromedriver' + \
    '\\chromedriver.exe'
TIMEOUT = 10 # seconds for implicit wait


class TestNotesReporterAPI(unittest.TestCase):

    def setUp(self):
        '''Starts Selenium WebDriver.'''
        self.driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
        # set implicit wait to 'TIMEOUT' seconds
        self. driver.implicitly_wait(TIMEOUT)

    def test_page_content(self):
        '''Assert that correct source is generated for the given API command.'''
        
        # note_reporter's API command to test
        API_CMD = 'http://localhost:5000/api/v1.0/results/2'
        
        # open the page to test
        self.driver.get(API_CMD)
        
        # retrieve page source as a string
        page_to_test_source = self.driver.page_source

        # read known good source for the given API command
        with open("good_source_2_results.txt", "r") as f:
            known_good_source = f.read()


        self.assertEqual(page_to_test_source, known_good_source)

    def tearDown(self):
        '''Stops Selenium WebDriver.'''
        # perform cleanup
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()