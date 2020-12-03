import time
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

vpnregions = ["de-frankfurt","de-berlin","belgium","austria","netherlands","romania","luxembourg","poland","denmark","switzerland","hungary","uk-london","uk-southampton","uk-manchester","czech-republic","italy","sweden","france","finland","ireland","norway","spain","israel","us-east","us-new-york-city","us-washington-dc","us-atlanta","us-chicago","us-houston","us-denver","us-texas","us-florida","us-west","us-silicon-valley","us-california","us-las-vegas","us-seattle","ca-montreal","ca-toronto","ca-vancouver","uae","mexico","hong-kong","singapore","au-melbourne","au-perth","au-sydney","japan","new-zealand"]
doubleCheck = False
currentVPNIndex = 0
driver = webdriver.Firefox()
driver.implicitly_wait(20)

def pageProcess():
	driver.get("https://sampleUrl.com")
	buttonUPD = driver.find_element_by_xpath('//p[@class="yp-info-action"]/a[text()="Request update"]') # find html element
	buttonUPD.click()
	time.sleep(15)
	print("Everything fine!!")
def changIP():
	global vpnregions, currentVPNIndex, doubleCheck
	doubleCheck = False
	totalVpncount = len(vpnregions)
	newVPN = vpnregions[currentVPNIndex]
	command = "piactl set region "+newVPN
	print("["+str(currentVPNIndex)+"/"+str(totalVpncount)+"]"+command)
	piapath = "c:\\Program Files\\Private Internet Access\\"
	os.chdir(piapath)
	os.system('cmd /c '+command)
	if (currentVPNIndex<totalVpncount):
		currentVPNIndex+=1
	else:
		currentVPNIndex=0
	time.sleep(15)

while True:
	try:
		changIP()
		pageProcess()
	except Exception:
		doubleCheck = True
	pass