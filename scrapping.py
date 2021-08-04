import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from googletrans import Translator, constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import cred
import json
import mysql.connector
PATH = "/Users/sweetygupta/desktop/chromedriver.exe"
# driver = webdriver.Chrome(executable_path='/Users/sweetygupta/desktop/chromedriver.exe')
translator = Translator()



mydb  = mysql.connector.connect(
    host ="127.0.0.1" , 
    user = "root" , 
    passwd="Mmsp13061402",
    database = "img" ,
    auth_plugin = "caching_sha2_password" ,
    port = 3306
    )


class Person:
    def __init__(self,name : str, city : str='' , work: list= []) :
        self.name = name
        self.city = city
        self.work = work

    def show(self) :
        print("Name: " + self.name)
        print("City: " +self.city)
        print("Work: " + ''.join(self.work))

    def upload(self, username):
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE user SET name=%s,work=%s,city=%s WHERE username=%s", (str(self.name), str(self.city) , json.dumps(self.work) , username))
        mydb.commit()


def find(result) :
    for res in result :
        # print(res[0])
        if(res[1] != ""):
            print(res[1])
            if(res[2] is not None) :
                if(res[3] is not None) :
                    return Person(name=res[1], city= res[2], work=res[3])
                else: 
                    return Person(name=res[1],city=res[2])
            else:
                if(res[3] is None):
                    return Person(name=res[1])
                    
                else:
                    return Person(name=res[1],work=res[3])
        else:
            return None
                    



def val(func):
    def inner(username):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user where username=\'" + username + "\'")

        myresult = mycursor.fetchall()
        scraped=0
        for res in myresult:
            scraped=1
        # if it exists in database
        if(scraped==0):
              raise ValueError("Invalid username")

        else:
            person = find(myresult)
            if(person is not None):
                person.show()
            else:
                func(username)

        return 

    return inner

@val
def scrap(username):
    name= srch_name(username)
    work= srch_work(username)

    city=srch_city(username)
    fav = srch_fav(username)
    p = Person(name, city, work)
    p.show()
    print("Favourites: ")
    print(fav)
    p.upload(username)

exist=0
def srch_name(username):
    url = "https://en-gb.facebook.com/{uname}".format(uname=username)
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    name= soup.title.get_text()
    return name

def srch_city(username):
    exist=0
    city = ""
    url = "https://m.facebook.com/{uname}/about/".format(uname= username)
    r = requests.get(url)
    htmlContent = r.text
    soup = BeautifulSoup(htmlContent , 'html.parser')
    divs = soup.find_all('div')
    for elem in divs :
        if (elem.string =="Places lived"):
            trgt =elem
            exist = 1
    if exist==1 :
        work_div = soup.find('div',  {"id" : "main_column"}).div
        citydiv = trgt.find_parent('div').next_sibling
        anchors = citydiv.find_all('a')
        city = anchors[0].get_text()
        # print(anchors[0].get_text())
        exist = 0
    return city

def srch_work(username):
    exist=0
    url = "https://m.facebook.com/{uname}/about/".format(uname= username)
    r = requests.get(url)
    htmlContent = r.text
    soup = BeautifulSoup(htmlContent , 'html.parser')
    divs = soup.find_all('div')
    work = []
    # print(soup.prettify())
    for elem in divs :
        if (elem.string =="Work"):
            trgt =elem
            exist = 1

    if exist==1 :
        # workdiv =trgt.find_parent("div" , {"id" : "main_column"}).children[0]
        workdiv = soup.find('div',  {"id" : "main_column"}).div.div
        anchors = workdiv.find_all('a')
        for i in range(1,len(anchors)) :
            # print("Work : " + anchors[i].get_text())
            work.append(anchors[i].get_text())
        exist=0
    return work




    
    # print(soup.prettify())
def srch_fav(username) :
    url = "https://m.facebook.com/{uname}/about/".format(uname= username)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_link_text('Log In').click()
    time.sleep(1)
    email = driver.find_element_by_id("m_login_email")
    pwd = driver.find_element_by_id("m_login_password")
    email.send_keys(cred.c.uname)
    pwd.send_keys(cred.c.password)
    time.sleep(0.3)
    pwd.send_keys(Keys.RETURN)
    time.sleep(2)
    # driver.find_element_by_id("checkpointSubmitButton-actual-button").click()
    # time.sleep(5)


    height1 = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        height2 = driver.execute_script("return document.body.scrollHeight")
        if height2 == height1 :
            break
        height1 = height2

    time.sleep(0.5)
    
    driver.find_element_by_xpath("//div[contains(text(),'Likes')]/../../div[3]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="timelineBody"]/div/div/div/div[1]/div/header/div/div[3]/a').click() 
    # All likes
    time.sleep(1)

    fav = {}

    all =[]

    for span in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[1]/div[*]/div/span'):
        all.append(span.text)

    for span in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[2]/div[*]/div/span'):
        all.append(span.text)
    # /html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[1]/div[1]
    fav['All likes'] = all
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[3]/a').click()
    time.sleep(0.5)
    sections = driver.find_elements_by_xpath('//*[@id="timelineBody"]/div/div/div/div[*]/div/header/div/div[3]/a')
    for sec in sections :
        sec.click()
        time.sleep(0.5)
        cat= driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/header/div/div/div/div/div[1]').text
        temp= []
        for span in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div[1]/div/span'):
            temp.append(span.text)
        fav[cat] = temp
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[3]/a').click()
        time.sleep(0.5)
        
        
        
    driver.quit()
    return fav
    


    

scrap("rishi.ranjan.54966")

# //*[@id="app_section100008055185321:2409997254"]/div/div/div/div/header/div/div[3]/a
# /html/body/div[1]/div[1]/div[4]/div/div/div/div[2]/div[12]/div/div/div/div/header/div/div[3]/a