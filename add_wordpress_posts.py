# -*- coding: utf8 -*-
# Python 2 yet
import os, random, time
from selenium import webdriver
dc = webdriver.DesiredCapabilities()
dc.__setattr__("unicodeKeyboard", "True")

website_root = "http://blank.ru"
start_page = "/wp-login.php"
admin_post_page = "/wp-admin/post-new.php"
login = ""
passwd = ""

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
browser.get(website_root + start_page)
time.sleep(3)

login_input = browser.find_element_by_xpath('.//input[@name="log"]')
login_input.send_keys(login)
pass_input = browser.find_element_by_xpath('.//input[@name="pwd"]')
pass_input.send_keys(passwd)
auth_button = browser.find_element_by_xpath('.//input[@name="wp-submit"]')
auth_button.click()
time.sleep(5)

i = 0
while i < 10:
    browser.get(website_root + admin_post_page)
    time.sleep(5)
    
    heading = browser.find_element_by_xpath('//input[@name="post_title"]')
    person_name = u"Тестовая запись"
    heading.send_keys(person_name)
    
    main_text = u"<p>Это <a href=\"#\">тестовая запись.</a> Пожалуйста, \
    не обращайте на нее внимания.</p><p>варыпшзрвашщзпр вшарпш вгарпш гваршп \
    грвашгпр вашгрп шаврш рп шварпшрвашпрвашпрвашпршваршпраш</p>\
    <p>sfjkgiojdfogjodf</p>"
    browser.execute_script("document.getElementsByTagName('textarea')[0].value='"
                           + main_text + "';")
    
    rubric = random.randint(3, 5)
    rubric_control = browser.find_element_by_xpath('//input[@id="in-category-' + str(rubric) + '"]')
    rubric_control.click()
    publish_button = browser.find_element_by_xpath('//input[@name="publish"]')
    publish_button.click()
    time.sleep(3)
    i += 1
