![GitHub](https://img.shields.io/github/license/estayparadox/insta-bot)
![GitHub top language](https://img.shields.io/github/languages/top/estayparadox/insta-bot)
![GitHub issues](https://img.shields.io/github/issues/estayparadox/insta-bot)
![GitHub contributors](https://img.shields.io/github/contributors/estayparadox/insta-bot)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/estayparadox/insta-bot/master)

# Insta-Bot

> An Instagram Bot developed in Python with Selenium which uses the follow back principle to bring you followers gradually.

## Increase your Instagram followers gradually
This bot is made to build an audience.
It's not a bot that will directly bring you thousands of followers but maybe dozens of them every days.
The principle is simple, the bot will search, thanks to a list of defined tags, for random posts on Instagram. For each post, the bot will like, comment and follow the author.
As with Twitter, many users often follow the people who follow them.
This bot therefore works on the « follow back » principle.

![image1](https://github.com/Estayparadox/InstaBot/blob/master/resource/IMG_1869.png)
![image2](https://github.com/Estayparadox/InstaBot/blob/master/resource/IMG_1872.png)
![image3](https://github.com/Estayparadox/InstaBot/blob/master/resource/IMG_1897.jpeg)

## How to use InstaBot

### 1. Prerequisites
To be able to run this little bot, you’ll need to have:
* [Python](https://www.python.org/downloads/)
* [Selenium](https://selenium-python.readthedocs.io/installation.html)
* [Chromedriver](http://chromedriver.chromium.org)
* [Geckodriver](https://github.com/mozilla/geckodriver)
* Google Chrome (English version) or Mozilla Firefox

### 2. Configuration
These two lines are designed to authenticate you on Instagram. Basically  change **your_username** and **your_password** to your Instagram credentials.
```python
username.send_keys('your_username')
...
password.send_keys('your_password')
```
This is the hashtags your bot will reach to find random posts and persons to comment / like / follow.
Change this line with your custom tags, here I’m using **trip**, **dronephotography** and **traveler** tags.
```python
hashtag_list = ['trip', 'dronephotography', 'traveler']
```

### 4. Install all libraries

You can install all the libraries and modules used in this project using the below command.  

```shell
pip install -r requirements.txt  
```

### 3. Run
Once the configuration is complete, it's time to run this bot.
Simply run the command line below in a terminal:
```shell
$> python start.py
```
