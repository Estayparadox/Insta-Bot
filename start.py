# ┌────────────────────────────────────────────────────────────────────────┐
# │ InstaBot - Python Selenium Bot                                         │
# ├────────────────────────────────────────────────────────────────────────┤
# │ Copyright © 2019 Joseph Pereniguez                                     |
# | (https://github.com/Estayparadox/InstaBot)                             │
# ├────────────────────────────────────────────────────────────────────────┤
# │ Licensed under the MIT                                                 |
# | (https://github.com/Estayparadox/InstaBot/blob/master/LICENSE) license.│
# └────────────────────────────────────────────────────────────────────────┘
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium.webdriver.common.by import By


#for firefoxdriver
# i = __file__.rfind('/')
# webdriver = webdriver.Firefox(executable_path=__file__[:i + 1] + 'geckodriver.exe')
#for chromedriver
# chromedriver_path ='/Users/josephpereniguez/Projects/InstaBot/chromedriver' # Change this to your own chromedriver path!
# webdriver = webdriver.Chrome(executable_path=chromedriver_path)

# define chrome driver path
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
webdriver = webdriver.Chrome(options=opt)

sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

username = webdriver.find_element_by_name('username')
username.send_keys('your_username') # Change this to your own Instagram username
password = webdriver.find_element_by_name('password')
password.send_keys('your_password') # Change this to your own Instagram password

button_login = webdriver.find_element(By.XPATH, '//html//body//div[1]//section//main//div//article//div//div[1]//div//form//div//div[3]//button//div')
button_login.click()
sleep(3)
try:
    notnow = webdriver.find_element(By.XPATH, '//html//body//div[1]//section//main//div//div//div//div//button')
    notnow.click() # Comment these last 2 lines out, if you don't get a pop up asking about notifications
except :
    pass
hashtag_list = ['trip', 'dronephotography', 'traveler'] # Change this to your own tags

prev_user_list = [] # If it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20190604-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(1,2))
    try:
        for x in range(1,200):

            username = webdriver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            if username not in prev_user_list:

                # If we already follow, do not unfollow
                if webdriver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow' :

                    webdriver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                    button_like.click()
                    likes += 1
                    sleep(randint(18,25))

                    # Comments and tracker
                    comm_prob = randint(1,10)
                    print('{}_{}: {}'.format(hashtag, x,comm_prob))
                    if comm_prob > 7:
                        comments += 1
                        webdriver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                        comment_box = webdriver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                        if comm_prob < 7:
                            comment_box.send_keys('Really cool!')
                            sleep(1)
                        elif (comm_prob > 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :)')
                            sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!!')
                            sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :)')
                            sleep(1)
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        sleep(randint(22, 28))

                # Next picture
                webdriver.find_element(By.LINK_TEXT, 'Next').click()
                sleep(randint(25, 29))
            else:
                webdriver.find_element(By.LINK_TEXT, 'Next').click()
                sleep(randint(20, 26))
    # Some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
