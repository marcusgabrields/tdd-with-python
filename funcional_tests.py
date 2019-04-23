from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has been talking about an interesting new online application for
        # list of tasks. She decides to check your homepage
        self.browser.get('http://localhost:8000')

        # She realizes that the title of the page and the 
        # header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to insert an immediate task item

        # She type "Buy peacock feathers" in a box
        # of text (Edith's hobby is to make baits for fly fishing)

        # When this key comes in, a page is hidden, and now a page is
        # "1: Buy feathered peacock" as an item in a to-do list

        # There is still a text box inviting it to another
        # item. She inserts "Use peacock feathers to make a fly"

        # The page is again and now shows the two items in your list

        # Edith wonders if the site remembers your list. So she notices
        # that the site generated a unique URL for it - there is a small
        # explanatory text is this

        # She accesses this URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()