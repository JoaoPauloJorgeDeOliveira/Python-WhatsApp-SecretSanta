import sys
from time import sleep

from selenium.webdriver import ActionChains

import whatsapp_api

# Xpaths
MoreContactsXPath = '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[5]/div[2]'
GroupInfoXPath = '// *[ @ id = "app"] / div / div / div[2] / div[3] / span / div / span / div / div / div[1]'

# Classes
nameClass = '_19RFN._1ovWX._F7Vk'
messageClass = '_12pGw'
messageMenuClass = '_2-qoA'
messageMenuButtonsClass = '_3zy-4.Sl-9e._3_4Kp'
eraseButtonsClass = '_2eK7W._23_1v'

class WhatsApp_JPO(whatsapp_api.WhatsApp):
    def get_group_members_short(self):
        """Get 1'st members' names (or numbers, if person is not in contact list) from a WhatsApp group"""
        try:
            el = self.driver.find_element_by_xpath(whatsapp_api.CONTACTS)
            return el.text.split(', ')
        except Exception as e:
            print("Group header not found")

    def get_group_members_long(self):
        """Get complete members' names (or numbers, if person is not in contact list) from a WhatsApp group"""
        try:
            # Click on contacts:
            el = self.driver.find_element_by_xpath(whatsapp_api.CONTACTS)
            # el = wp.driver.find_element_by_xpath(whatsapp_api.CONTACTS)
            el.click()
            sleep(3)

            # Trying to click in more contacts (it may not exist)
            try:
                el = self.driver.find_element_by_xpath(MoreContactsXPath)
                # el = wp.driver.find_element_by_xpath(MoreContactsXPath)
                el.click()
            except Exception as e:
                msg = 'Error in {}.{}. Message: {}'.format(
                    self.__class__.__name__,            # Ref. for getting class name on 2019-06-26:  https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                    sys._getframe().f_code.co_name,     # Ref. for getting method name on 2019-06-26: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
                    e)
                print(msg)

            el1 = self.driver.find_element_by_xpath(GroupInfoXPath) # Getting element for Group Info box panel.
            # el1 = wp.driver.find_element_by_xpath(GroupInfoXPath)   # Getting element for Group Info box panel.
            el2 = el1.find_elements_by_class_name(nameClass)        # Locating all elements of such class inside el1.
            Members = [e.text for e in el2]                         # Getting only the texts, not the whole objects.
            # Members = Members[::2]                                  # Getting every other element to remove descriptions. Ref: https://stackoverflow.com/questions/8865878/skipping-every-other-element-after-the-first

            return Members

        except Exception as e:
            msg = 'Error in {}.{}. Message: {}'.format(
                self.__class__.__name__,
                # Ref. for getting class name on 2019-06-26:  https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                sys._getframe().f_code.co_name,
                # Ref. for getting method name on 2019-06-26: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
                e)
            print(msg)

    def get_all_messages_elements(self):
        """Gets all messages currently shown in screen."""
        all_messages_element = self.driver.find_elements_by_class_name(messageClass)
        return all_messages_element

    def delete_message_from_recent(self, text):
        """From recent (visible) messages, deletes the one with text equals to 'text'."""
        try:
            all_messages_element = self.get_all_messages_elements()     # Getting all recent messages.
            # all_messages_element = wp.get_all_messages_elements()

            for e in reversed(all_messages_element):                    # Looking at each element in reversed order.
                if e.text == text:
                    # Moving mouse over message, so menu appear. Ref: http://allselenium.info/mouse-over-actions-using-python-selenium-webdriver/
                    action = ActionChains(self.driver)
                    # action = ActionChains(wp.driver)
                    action.move_to_element(e).perform()
                    sleep(1)

                    # Clicking on menu
                    msgMenu = self.driver.find_elements_by_class_name(messageMenuClass)
                    # msgMenu = wp.driver.find_elements_by_class_name(messageMenuClass)
                    msgMenu[0].click()
                    sleep(1)

                    # Clicking on delete button:
                    msgMenuButtons = self.driver.find_elements_by_class_name(messageMenuButtonsClass)   # Getting buttons
                    # msgMenuButtons = wp.driver.find_elements_by_class_name(messageMenuButtonsClass)
                    msgMenuButtons[-1].click()                                                          # Clicking on last button.
                    sleep(1)

                    # Clicking on 'Erase for me' button:
                    eraseButtons = self.driver.find_elements_by_class_name(eraseButtonsClass)   # Getting buttons
                    # eraseButtons = wp.driver.find_elements_by_class_name(eraseButtonsClass)   # Getting buttons
                    eraseButtons[0].click()                                                     # Clicking on first button.

                    break                                                                       # After deleting last msg that corresponds to 'text', breaks for loop.
            else:
                print('Did not find recent message with text: ' + text)

        except Exception as e:
            msg = 'Error in {}.{}. Message: {}'.format(
                self.__class__.__name__,            # Ref. for getting class name on 2019-06-26:  https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                sys._getframe().f_code.co_name,     # Ref. for getting method name on 2019-06-26: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
                e)
            print(msg)