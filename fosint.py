import platform
from clint.textui import colored
from time import sleep
import os
import webbrowser

def printg(a):
        print(colored.green(a))

def Windows():
	for x in range(0, 6):
                os.system("cls")
                if(x == 0):
                        print(colored.green("| Loading Facebook OSINT Tool! |"))
                elif(x == 1):
                        print(colored.white("/ Loading Facebook OSINT Tool! /"))
                elif(x == 2):
                        print(colored.yellow("- Loading Facebook OSINT Tool! -"))
                elif(x == 3):
                        print(colored.green("\\ Loading Facebook OSINT Tool! \\"))
                elif(x == 4):
                        print(colored.white("| Loading Facebook OSINT Tool! |"))
                elif(x == 5):
                        print(colored.yellow("/ Loading Facebook OSINT Tool! /"))
                sleep(0.7)
	os.system("cls")
	printg("Welcome to the Facebook Open Sourced Intelligence Tool, written by CyberViking and converted to python by AlanTheBlank")
	sleep(0.5)
	printg("This tool will log the searches used in your Facebook search history so usage of an alt account is recommended")
	sleep(0.5)
	printg("Please press 1 to open a site to get the Facebook ID, or press any key to enter the ID")
	a = input()
	if(a == '1'):
		webbrowser.open_new_tab("http://sluppend.com/3OO8")
	os.system("cls")
	printg("Please enter the UserID")
	Id = input()
	printg("The UserID entered is " + Id)
	running = True
	main = True
	profile = False
	interests = False
	likes = False
	places = False
	connections = False
	comments = False
	tags = False
	while(running):
		if(main):
			os.system("cls")
			printg("Facebook UserID is " + Id + ".  To change it enter 13")
			printg("Enter 1 for profile information")
			printg("Enter 2 for interests")
			printg("Enter 3 for likes")
			printg("Enter 4 for places")
			printg("Enter 5 for connections")
			printg("Enter 6 for comments")
			printg("Enter 7 for tags")
			printg("Enter 0 to exit")
			b = int(input())
			if(b == 1):
				profile = True
				main = False
			if(b == 2):
				interests = True
				main = False
			if(b == 3):
				likes = True
				main = False
			if(b == 4):
				places = True
				main = False
			if(b == 5):
				connections = True
				main = False
			if(b == 6):
				comments = True
				main = False
			if(b == 7):
				tags = True
				main = False
			if(b == 0):
				exit(0)
			if(b == 13):
				webbrowser.open_new_tab("http://sluppend.com/3OO8")
				printg("Please enter the new ID")
				Id = input()
		if(tags):
			os.system("cls")
			printg("Enter 1 for tagged photos")
			printg("Enter 2 for tagged videos")
			printg("Enter 3 for tagged posts")
			printg("Enter 4 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-of/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-of/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-tagged/intersect")
			if(b == 4):
				main = True
				tags = False
		if(comments):
			os.system("cls")
			printg("Enter 1 for photos commented on")
			printg("Enter 2 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-commented/intersect")
			if(b == 2):
				main = True
				comments = False
				
		if(connections):
			os.system("cls")
			printg("Enter 1 for relatives")
			printg("Enter 2 for friends")
			printg("Enter 3 for friends of friends")
			printg("Enter 4 for coworkers")
			printg("Enter 5 for school friends")
			printg("Enter 6 for friends in current city")
			printg("Enter 7 to return to main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/relatives/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/friends/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/friends/friends/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/employees/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/schools-attended/ever-past/intersect/students/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/current-cities/residents-near/present/intersect")
			if(b == 7):
				main = True
				connections = False
		if(likes):
			os.system("cls")
			printg("Enter 1 for liked photos")
			printg("Enter 2 for liked videos")
			printg("Enter 3 for liked stories")
			printg("Enter 4 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-liked/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-liked/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-liked/intersect")
			if(b == 4):
				main = True
				likes = False
		if(places):
			os.system("cls")
			printg("Enter 1 for places visited")
			printg("Enter 2 for bars visited")
			printg("Enter 3 for restraunts visited")
			printg("Enter 4 for cinemas visited")
			printg("Enter 5 for hotels visited")
			printg("Enter 6 for locations visited")
			printg("Enter 7 for shops visited")
			printg("Enter 8 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/110290705711626/places/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/273819889375819/places/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/192511100766680/places/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/164243073639257/places/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/935165616516865/places/intersect")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/200600219953504/places/intersect")
			if(b == 8):
				main = True
				places = False
		if(interests):
			os.system("cls")
			printg("Enter 1 for pages liked")
			printg("Enter 2 for restraunts liked")
			printg("Enter 3 for religious pages liked")
			printg("Enter 4 for music liked")
			printg("Enter 5 for movies liked")
			printg("Enter 6 for books liked")
			printg("Enter 7 for places liked")
			printg("Enter 8 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/161431733929266/pages/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/religion/pages/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/musician/pages/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/movie/pages/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/book/pages/intersect")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-liked")
			if(b == 8):
				main = True
				interests = False
		if(profile):
			os.system("cls")
			printg("Enter 1 for apps")
			printg("Enter 2 for games")
			printg("Enter 3 for events")
			printg("Enter 4 for upcoming events")
			printg("Enter 5 for groups")
			printg("Enter 6 for posts")
			printg("Enter 7 for videos")
			printg("Enter 8 for pictures")
			printg("Enter 9 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/apps-used")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/apps-used/apps/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/events-joined/in-past/date/events/intersect/")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/events-joined/")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/groups")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-by/")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-by/")
			if(b == 8):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-by/")
			if(b == 9):
				main = True
				profile = False
def Linux():
	for x in range(0, 6):
                os.system("clear")
                if(x == 0):
                        print(colored.green("| Loading Facebook OSINT Tool! |"))
                elif(x == 1):
                        print(colored.white("/ Loading Facebook OSINT Tool! /"))
                elif(x == 2):
                        print(colored.yellow("- Loading Facebook OSINT Tool! -"))
                elif(x == 3):
                        print(colored.green("\\ Loading Facebook OSINT Tool! \\"))
                elif(x == 4):
                        print(colored.white("| Loading Facebook OSINT Tool! |"))
                elif(x == 5):
                        print(colored.yellow("/ Loading Facebook OSINT Tool! /"))
                sleep(1)
	os.system("clear")
	printg("Welcome to the Facebook Open Sourced Intelligence Tool, written by CyberViking and converted to python by AlanTheBlank")
	sleep(0.5)
	printg("This tool will log the searches used in your Facebook search history so usage of an alt account is recommended")
	sleep(0.5)
	printg("Please press 1 to open a site to get the Facebook ID, or press any key to enter the ID")
	a = input()
	if(a == '1'):
		webbrowser.open_new_tab("http://sluppend.com/3OO8")
	os.system("clear")
	printg("Please enter the UserID")
	Id = input()
	printg("The UserID entered is " + Id)
	running = True
	main = True
	profile = False
	interests = False
	likes = False
	places = False
	connections = False
	comments = False
	tags = False
	while(running):
		if(main):
			os.system("clear")
			printg("Facebook UserID is " + Id + ".  To change it enter 13")
			printg("Enter 1 for profile information")
			printg("Enter 2 for interests")
			printg("Enter 3 for likes")
			printg("Enter 4 for places")
			printg("Enter 5 for connections")
			printg("Enter 6 for comments")
			printg("Enter 7 for tags")
			printg("Enter 0 to exit")
			b = int(input())
			if(b == 1):
				profile = True
				main = False
			if(b == 2):
				interests = True
				main = False
			if(b == 3):
				likes = True
				main = False
			if(b == 4):
				places = True
				main = False
			if(b == 5):
				connections = True
				main = False
			if(b == 6):
				comments = True
				main = False
			if(b == 7):
				tags = True
				main = False
			if(b == 0):
				exit(0)
			if(b == 13):
				webbrowser.open_new_tab("http://sluppend.com/3OO8")
				printg("Please enter the new ID")
				Id = input()
		if(tags):
			os.system("clear")
			printg("Enter 1 for tagged photos")
			printg("Enter 2 for tagged videos")
			printg("Enter 3 for tagged posts")
			printg("Enter 4 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-of/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-of/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-tagged/intersect")
			if(b == 4):
				main = True
				tags = False
		if(comments):
			os.system("clear")
			printg("Enter 1 for photos commented on")
			printg("Enter 2 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-commented/intersect")
			if(b == 2):
				main = True
				comments = False
				
		if(connections):
			os.system("clear")
			printg("Enter 1 for relatives")
			printg("Enter 2 for friends")
			printg("Enter 3 for friends of friends")
			printg("Enter 4 for coworkers")
			printg("Enter 5 for school friends")
			printg("Enter 6 for friends in current city")
			printg("Enter 7 to return to main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/relatives/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/friends/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/friends/friends/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/employees/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/schools-attended/ever-past/intersect/students/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/current-cities/residents-near/present/intersect")
			if(b == 7):
				main = True
				connections = False
		if(likes):
			os.system("clear")
			printg("Enter 1 for liked photos")
			printg("Enter 2 for liked videos")
			printg("Enter 3 for liked stories")
			printg("Enter 4 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-liked/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-liked/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-liked/intersect")
			if(b == 4):
				main = True
				likes = False
		if(places):
			os.system("clear")
			printg("Enter 1 for places visited")
			printg("Enter 2 for bars visited")
			printg("Enter 3 for restraunts visited")
			printg("Enter 4 for cinemas visited")
			printg("Enter 5 for hotels visited")
			printg("Enter 6 for locations visited")
			printg("Enter 7 for shops visited")
			printg("Enter 8 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/110290705711626/places/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/273819889375819/places/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/192511100766680/places/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/164243073639257/places/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/935165616516865/places/intersect")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/200600219953504/places/intersect")
			if(b == 8):
				main = True
				places = False
		if(interests):
			os.system("clear")
			printg("Enter 1 for pages liked")
			printg("Enter 2 for restraunts liked")
			printg("Enter 3 for religious pages liked")
			printg("Enter 4 for music liked")
			printg("Enter 5 for movies liked")
			printg("Enter 6 for books liked")
			printg("Enter 7 for places liked")
			printg("Enter 8 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/161431733929266/pages/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/religion/pages/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/musician/pages/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/movie/pages/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/book/pages/intersect")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-liked")
			if(b == 8):
				main = True
				interests = False
		if(profile):
			os.system("clear")
			printg("Enter 1 for apps")
			printg("Enter 2 for games")
			printg("Enter 3 for events")
			printg("Enter 4 for upcoming events")
			printg("Enter 5 for groups")
			printg("Enter 6 for posts")
			printg("Enter 7 for videos")
			printg("Enter 8 for pictures")
			printg("Enter 9 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/apps-used")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/apps-used/apps/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/events-joined/in-past/date/events/intersect/")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/events-joined/")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/groups")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-by/")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-by/")
			if(b == 8):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-by/")
			if(b == 9):
				main = True
				profile = False
				
def Mac():
	for x in range(0, 6):
                os.system("clear")
                if(x == 0):
                        print(colored.green("| Loading Facebook OSINT Tool! |"))
                elif(x == 1):
                        print(colored.white("/ Loading Facebook OSINT Tool! /"))
                elif(x == 2):
                        print(colored.yellow("- Loading Facebook OSINT Tool! -"))
                elif(x == 3):
                        print(colored.green("\\ Loading Facebook OSINT Tool! \\"))
                elif(x == 4):
                        print(colored.white("| Loading Facebook OSINT Tool! |"))
                elif(x == 5):
                        print(colored.yellow("/ Loading Facebook OSINT Tool! /"))
                sleep(1)
	os.system("clear")
	printg("Welcome to the Facebook Open Sourced Intelligence Tool, written by CyberViking and converted to python by AlanTheBlank")
	sleep(0.5)
	printg("This tool will log the searches used in your Facebook search history so usage of an alt account is recommended")
	sleep(0.5)
	printg("Please press 1 to open a site to get the Facebook ID, or press any key to enter the ID")
	a = input()
	if(a == '1'):
		webbrowser.open_new_tab("http://sluppend.com/3OO8")
	os.system("clear")
	printg("Please enter the UserID")
	Id = input()
	printg("The UserID entered is " + Id)
	running = True
	main = True
	profile = False
	interests = False
	likes = False
	places = False
	connections = False
	comments = False
	tags = False
	while(running):
		if(main):
			os.system("clear")
			printg("Facebook UserID is " + Id + ".  To change it enter 13")
			printg("Enter 1 for profile information")
			printg("Enter 2 for interests")
			printg("Enter 3 for likes")
			printg("Enter 4 for places")
			printg("Enter 5 for connections")
			printg("Enter 6 for comments")
			printg("Enter 7 for tags")
			printg("Enter 0 to exit")
			b = int(input())
			if(b == 1):
				profile = True
				main = False
			if(b == 2):
				interests = True
				main = False
			if(b == 3):
				likes = True
				main = False
			if(b == 4):
				places = True
				main = False
			if(b == 5):
				connections = True
				main = False
			if(b == 6):
				comments = True
				main = False
			if(b == 7):
				tags = True
				main = False
			if(b == 0):
				exit(0)
			if(b == 13):
				webbrowser.open_new_tab("http://sluppend.com/3OO8")
				printg("Please enter the new ID")
				Id = input()
		if(tags):
			os.system("clear")
			printg("Enter 1 for tagged photos")
			printg("Enter 2 for tagged videos")
			printg("Enter 3 for tagged posts")
			printg("Enter 4 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-of/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-of/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-tagged/intersect")
			if(b == 4):
				main = True
				tags = False
		if(comments):
			os.system("clear")
			printg("Enter 1 for photos commented on")
			printg("Enter 2 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-commented/intersect")
			if(b == 2):
				main = True
				comments = False
				
		if(connections):
			os.system("clear")
			printg("Enter 1 for relatives")
			printg("Enter 2 for friends")
			printg("Enter 3 for friends of friends")
			printg("Enter 4 for coworkers")
			printg("Enter 5 for school friends")
			printg("Enter 6 for friends in current city")
			printg("Enter 7 to return to main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/relatives/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/friends/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/friends/friends/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/employees/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/schools-attended/ever-past/intersect/students/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/current-cities/residents-near/present/intersect")
			if(b == 7):
				main = True
				connections = False
		if(likes):
			os.system("clear")
			printg("Enter 1 for liked photos")
			printg("Enter 2 for liked videos")
			printg("Enter 3 for liked stories")
			printg("Enter 4 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-liked/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-liked/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-liked/intersect")
			if(b == 4):
				main = True
				likes = False
		if(places):
			os.system("clear")
			printg("Enter 1 for places visited")
			printg("Enter 2 for bars visited")
			printg("Enter 3 for restraunts visited")
			printg("Enter 4 for cinemas visited")
			printg("Enter 5 for hotels visited")
			printg("Enter 6 for locations visited")
			printg("Enter 7 for shops visited")
			printg("Enter 8 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/110290705711626/places/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/273819889375819/places/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/192511100766680/places/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/164243073639257/places/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/935165616516865/places/intersect")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-visited/200600219953504/places/intersect")
			if(b == 8):
				main = True
				places = False
		if(interests):
			os.system("clear")
			printg("Enter 1 for pages liked")
			printg("Enter 2 for restraunts liked")
			printg("Enter 3 for religious pages liked")
			printg("Enter 4 for music liked")
			printg("Enter 5 for movies liked")
			printg("Enter 6 for books liked")
			printg("Enter 7 for places liked")
			printg("Enter 8 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/intersect")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/161431733929266/pages/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/religion/pages/intersect")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/musician/pages/intersect")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/movie/pages/intersect")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/pages-liked/book/pages/intersect")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/places-liked")
			if(b == 8):
				main = True
				interests = False
		if(profile):
			os.system("clear")
			printg("Enter 1 for apps")
			printg("Enter 2 for games")
			printg("Enter 3 for events")
			printg("Enter 4 for upcoming events")
			printg("Enter 5 for groups")
			printg("Enter 6 for posts")
			printg("Enter 7 for videos")
			printg("Enter 8 for pictures")
			printg("Enter 9 to return to the main menu")
			b = int(input())
			if(b == 1):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/apps-used")
			if(b == 2):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/apps-used/apps/intersect")
			if(b == 3):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/events-joined/in-past/date/events/intersect/")
			if(b == 4):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/events-joined/")
			if(b == 5):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/groups")
			if(b == 6):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/stories-by/")
			if(b == 7):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/videos-by/")
			if(b == 8):
				webbrowser.open_new_tab("https://www.facebook.com/search/" + Id + "/photos-by/")
			if(b == 9):
				main = True
				profile = False
				
if __name__ == "__main__":
	Os = platform.system()
	print(Os)
	if(Os == "Windows"):
		Windows()
	elif(Os == "Linux"):
		Linux()
	elif(Os == "Mac"):
		Mac()
	else:
		print("Unsupported OS!")
