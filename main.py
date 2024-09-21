from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random
from pyautogui import write
from ans import *

web = webdriver.Chrome()
url=''
web.get(url)

counter=412


###################### 233 Chapter ##########################
    # def extract_data_values(driver):
    #     """Extracts data-value attributes from div elements and returns a list."""

    #     # Find all div elements with the specified class
    #     div_elements = driver.find_elements(By.CSS_SELECTOR, '.MocG8c.HZ3kWc.mhLiyf.OIC90c.LMgvRb')

    #     data_values = []
    #     for div in div_elements:
    #         data_value = div.get_attribute('data-value')
    #         data_values.append(data_value)

    #     return data_values

    # # # Example usage:
    # values = extract_data_values(web)
    # print(len(values))
    # print(values[0])

chapters=233



while True:

    time.sleep(1)

    name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(random.choice(names))
    # time.sleep(1)


#####################################################

    gender=[]
    gender.append(web.find_element('xpath', '//*[@id="i9"]') )
    gender.append(web.find_element('xpath', '//*[@id="i12"]') )
    gender.append(web.find_element('xpath', '//*[@id="i15"]') )
 
    random.choice(gender).click()
    # gender[2].click()
    # time.sleep(1)
######################################################
   
    dropdown_element = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]')
    dropdown_element.click()
    
    option_number = random.randrange(chapters)

    for _ in range(option_number):
        write(['down'])
    write(['enter'])
    
    time.sleep(1)
################################################################

    next= web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    next.click()

    time.sleep(1)
##################################################################

    satisfaction=[]
    satisfaction.append(web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div') )
    satisfaction.append(web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div') )
    satisfaction.append(web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div') )

    random.choice(satisfaction).click()
    # time.sleep(1)

######################################################################

    recommend=[]
    recommend.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div'))
    recommend.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div'))
    recommend.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div'))

    random.choice(recommend).click()
    # time.sleep(1)

##########################################################################

    quality=[]
    quality.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div'))
    quality.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div'))
    quality.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div'))

    random.choice(quality).click()
    # time.sleep(1)
##############################################################################

    confident=[]
    confident.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div'))
    confident.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div'))
    confident.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div'))

    random.choice(confident).click()
    # time.sleep(1)

###############################################################################

    swag = web.find_element('xpath','//*[@id="i31"]')
    another_best=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[7]/div/div/div/div/div[1]/input')

    random_number = random.randint(1, 3)
    if random_number == 1:
        swag.click()
    elif random_number == 2:
        another_best.send_keys(random.choice(another_best_ans))
    else:
        swag.click()
        another_best.send_keys(random.choice(another_best_ans))
    time.sleep(1)
################################################################################

    plan= web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[5]/div/span/div/div/div[1]/input')
    plan.send_keys(random.choice(plan_ans))

    time.sleep(1)
####################################################################################

    future=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea')
    future.send_keys(random.choice(future_ans))

    time.sleep(1)
#####################################################################################

    loved=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea')
    loved.send_keys(random.choice(loved_ans))

    time.sleep(1)
#####################################################################################

    submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    submit.click()

    time.sleep(1)
#####################################################################

    resubmit=web.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
    resubmit.click()
    
    time.sleep(1)

    counter=counter+1
    print(counter)
    





    




