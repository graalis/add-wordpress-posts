# -*- coding: utf8 -*-
import os, random, time
from selenium import webdriver
dc = webdriver.DesiredCapabilities()
dc.__setattr__("unicodeKeyboard", "True")

start_url = "http://localhost"
start_page = "/wp-login.php"
admin_post_page = "/wp-admin/post-new.php"
login = ""
passwd = ""

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
browser.get(start_url)
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
    browser.get(start_url + admin_post_page)
    time.sleep(3)

    body = browser.find_element_by_xpath('//body')
    body.send_keys(u'\ue009', u'\ue008', u'\ue00a', "m");
    time.sleep(2)

    main_text = u"<p>Это <a href=\"#\">тестовая запись.</a> \
Пожалуйста, не обращайте на нее внимания.</p>\
<p>варыпшзрвашщзпр вшарпш вгарпш гваршп грвашгпр вашгрп шаврш рп\
шварпшрвашпрвашпрвашпршваршпраш</p><p>sfjkgiojdfogjodf</p>"
    browser.execute_script("document.getElementsByTagName('textarea')[1].value='"
                           + main_text + "';")
    time.sleep(2)

    heading = u"Тестовая запись"
    browser.execute_script("document.getElementsByTagName('textarea')[0].value = '"
                           + heading + "';")
    browser.execute_script("document.getElementsByTagName('button')[20].click();")
    time.sleep(3)
    browser.execute_script("document.getElementById('editor-post-taxonomies-hierarchical-term-2').checked=1;")
    time.sleep(3)
    
    browser.execute_script("document.getElementsByClassName('editor-post-publish-panel__toggle')[0].click();");
    time.sleep(3)
    browser.execute_script("document.getElementsByClassName('editor-post-publish-panel__toggle')[0].click();");
    time.sleep(100)
    i += 1
