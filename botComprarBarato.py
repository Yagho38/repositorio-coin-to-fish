import cv2
import pyautogui
import time
import random
import keyboard
import pyscreenshot 
from win10toast import ToastNotifier



def run():
	jafoi = 1
	jatirei = 0
	toaster = ToastNotifier()
	while True:
		"""if jafoi == 0:
			imgInventory = cv2.imread("inventory.png")
			coordinatesInventory = pyautogui.locateOnScreen(imgInventory)
			pyautogui.click(coordinatesInventory)
			time.sleep(10)
			if jatirei == 0:
				image = pyscreenshot.grab(bbox=(100, 300, 300, 400))
				image.save("saldo.png")
				imgSaldo = cv2.imread("saldo.png")
				jatirei = 1
				time.sleep(7)
			coordinatesSaldo = pyautogui.locateOnScreen(imgSaldo)
			if coordinatesSaldo == None:
				imgUrl = cv2.imread("url.png")
				coordinatesUrl = pyautogui.locateOnScreen(imgUrl)
				pyautogui.click(coordinatesUrl)
				pyautogui.write('https://cointofish.io/market', interval=0.25)
				pyautogui.press('enter')
				time.sleep(2.5)
				imgItems = cv2.imread("items.png")
				coordinatesItems = pyautogui.locateOnScreen(imgItems)
				pyautogui.click(coordinatesItems)
				time.sleep(2.5)
				imgAll = cv2.imread("all.png")
				coordinatesAll = pyautogui.locateOnScreen(imgAll)
				pyautogui.click(coordinatesAll)
				time.sleep(0.5)
				imgApple = cv2.imread("bread.png")
				coordinatesApple = pyautogui.locateOnScreen(imgApple)
				pyautogui.click(coordinatesApple)
				time.sleep(2.5)
				imgSortByDate = cv2.imread("sortbydate.png")
				coordinatesSortByDate = pyautogui.locateOnScreen(imgSortByDate)
				pyautogui.click(coordinatesSortByDate)
				time.sleep(0.5)
				imgSortByPrice = cv2.imread("sortbyprice.png")
				coordinatesSortByPrice = pyautogui.locateOnScreen(imgSortByPrice)
				pyautogui.click(coordinatesSortByPrice)
				time.sleep(2.5)
				jafoi = 1"""
		if jafoi == 1:
			img = cv2.imread("teste2.png") 
			coordinates1 = pyautogui.locateOnScreen(img)
			print(coordinates1)
			pyautogui.click(coordinates1)
			time.sleep(0.3)
			img2 = cv2.imread("teste3.png")
			coordinates = pyautogui.locateOnScreen(img2)
			print(coordinates)
			screenWidth, screenHeight = pyautogui.size()
			if coordinates != None:
				pyautogui.click(coordinates)
				time.sleep(0.31)
				img3 = cv2.imread("buy.png")
				coordinates2 = pyautogui.locateOnScreen(img3)
				print(coordinates2)
				if coordinates2 != None:
					pyautogui.click(coordinates2)
					time.sleep(2)
					img4 = cv2.imread("success.png")
					coordinates4 = pyautogui.locateOnScreen(img4)
					if coordinates4 != None:
						#jafoi = 2
						toaster.show_toast("✅Sucesso✅",
	                   "Mais um Comprado!",
	                   duration=5)
					else:
						toaster.show_toast("❌ERRO❌",
	                   "Deu ruim na hora de comprar!",
	                   duration=5)
		"""if jafoi == 2:
			imgUrl = cv2.imread("url.png")
			coordinatesUrl = pyautogui.locateOnScreen(imgUrl)
			pyautogui.click(coordinatesUrl)
			pyautogui.write('https://cointofish.io/home', interval=0.25)
			pyautogui.press('enter')
			time.sleep(2.5)
			imgInventory = cv2.imread("inventory.png")
			coordinatesInventory = pyautogui.locateOnScreen(imgInventory)
			pyautogui.click(coordinatesInventory)
			time.sleep(4)
			pyautogui.scroll(-1000)
			time.sleep(4)
			imgexpBread = cv2.imread("expBread.png")
			coordinatesexpBread = pyautogui.locateOnScreen(imgexpBread)
			pyautogui.click(coordinatesexpBread)
			time.sleep(2)
			imgpriceWrite = cv2.imread("priceWrite.png")
			coordinatespriceWrite = pyautogui.locateOnScreen(imgpriceWrite)
			pyautogui.click(coordinatespriceWrite)
			time.sleep(1)
			pyautogui.press('backspace')
			pyautogui.write('3', interval=0.25)
			time.sleep(1)
			imgquantityWrite = cv2.imread("quantityWrite.png")
			coordinatesquantityWrite = pyautogui.locateOnScreen(imgquantityWrite)
			pyautogui.click(coordinatesquantityWrite)
			time.sleep(1)
			pyautogui.press('backspace', presses=4)
			pyautogui.write('20', interval=0.25)
			time.sleep(1)
			imgsell = cv2.imread("sell.png")
			coordinatessell = pyautogui.locateOnScreen(imgsell)
			pyautogui.click(coordinatessell)
			jatirei = 0
			jafoi = 0
			toaster.show_toast("✅Sucesso✅",
                   "Mais um Comprado!",
                   duration=5)
			pyautogui.press('f5')
			time.sleep(10)"""
				
		if keyboard.is_pressed('ESC'):
			break
		
run()