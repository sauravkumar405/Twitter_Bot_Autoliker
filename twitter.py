#tkinter- will be used for gui which will take input frrom the user
#selenium- used to login and for some the javascript lines to scroll the screen
#pyautogui- to hit thaat hard button for auto like
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary




class twitter_bot:
	def __init__(self,username,password):
		self.username=username
		self.password=password
		#self.bot=webdriver.Firefox()
		self.bot = webdriver.Firefox(executable_path=r'C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\geckodriver.exe')


	def login(self):
		bot=self.bot
		bot.get('https://twitter.com/login')
		time.sleep(2)
		email=bot.find_element_by_name('session[username_or_email]')
		password=bot.find_element_by_name('session[password]')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(2)


	def like_tweet(self,entry3):
		bot=self.bot
		bot.get('https://twitter.com/search?q=%23'+str(entry3)+'&src=typed_query')
		

		while True:
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)
			pyautogui.click(pyautogui.locateCenterOnScreen('srv.png',grayscale=True),duration=2);
			time.sleep(2)

def execute():
	log=twitter_bot(str(entry1.get()),str(entry2.get()))
	log.login()
	log.like_tweet(entry3.get())


#binary = FirefoxBinary('C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\geckodriver.exe')

window=Tk()
window.geometry("700x600")
emails=Label(window,text="Enter your Username/E-Mail ID here",font='times 24 bold')
emails.grid(row=0,column=2)
entry1=Entry(window)
entry1.grid(row=1,column=4)

password=Label(window,text="Enter your Password here",font='times 24 bold')
password.grid(row=3,column=2)
entry2=Entry(window)
entry2.grid(row=3,column=4)

hashtag=Label(window,text="Enter your #Hashtag here",font='times 24 bold')
hashtag.grid(row=5,column=2)
entry3=Entry(window)
entry3.grid(row=3,column=4)
entry3.config(show="*")

b1=Button(window,text=" GO ",command=execute,width=12,bg='gray')
b1.grid(row=7,column=4)
window.mainloop()


