import os,sys,time
def loading(e):
	for a in e + "\n":
		sys.stdout.flush()
		sys.stdout.write(a)
		time.sleep(000.01)

def logo():
	os.system("clear")
	banner = """
\033[1;32m
____ _  _ ___ ____ ____     _  _ ____ _   _
|___  \/   |  |__/ |__|     |_/  |___  \_/
|___ _/\_  |  |  \ |  | ___ | \_ |___   |\033[1;31m
————————————————————————————————————————————\033[1;33m
<\> code by : \033[4mAriefDev\033[0m\033[1;33m
<\> team    : \033[4mBorneoExploit\033[0m\033[1;31m
————————————————————————————————————————————\033[0m
"""
	print (banner)
def menu():
	logo()
	print ("(01).Default")
	print ("(02).Two rows")
	print ("(03).configure")
	print ("(04).Exit/Close\n")

	menu = input("[•] choose >> ")
	if menu == "1" or menu == "01":
		default()
	elif menu == "2" or menu == "02":
		two()
	elif menu == "03" or menu == "3":
		configure()
	elif menu == "4" or menu == "04":
		loading("[•] Exit/Close .....")
		sys.exit()


def default():
	print ("————————————————————————————")
	loading("[•] add extra key ....")
	file = open("termux.properties","w")
	sc = """# code by : AriefDev
# team : BorneoExploit
# github : https://www.githuh.com/BorneoExploit
extra-keys = [[ESC, TAB, CTRL, ALT, {key: '-', popup: '|'}, DOWN, UP]]
"""
	file.write(sc)
	file.close()
	loading("[•] Refreshing ....")
	print ("————————————————————————————")
	os.system("mv termux.properties /$HOME/.termux && termux-reload-settings")
	print ("[%s]" % (time.strftime("%x")),"done...")
	print ("[%s] please restart termux app!" % (time.strftime("%x")))
	back = input("[%s] back " % (time.strftime("%x")))
	menu()

def two():
	print ("————————————————————————————")
	loading("[•] add extra key ...")
	file = open("termux.properties","w")
	sc = """# code by : AriefDev
# team   : BorneoExploit
# github : https://www.github.com/BorneoExploit
extra-keys = [['ESC','/','-','HOME','UP','END','KEYBOARD'], \['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','ENTER']]
"""
	file.write(sc)
	file.close()
	loading("[•] Refreshing ... ")
	print ("————————————————————————————")
	os.system("mv termux.properties /$HOME/.termux && termux-reload-settings")
	print ("[%s] done ..." % (time.strftime("%x")))
	print ("[%s] please restart termux app!" % (time.strftime("%x")))
	back = input("[%s] back " % (time.strftime("%x")))
	menu()

def configure():
	loading("————————————————————————")
	print ("[•] add extra key ... ")
	file = open("termux.properties","w")
	sc = """# code by : AriefDev
# team   : BorneoExploit
# github : https://www.github.com/BorneoExploit
extra-keys = [[   {key: ESC, popup: {macro: "CTRL f d", display: "tmux exit"}},   {key: CTRL, popup: {macro: "CTRL f BKSP", display: "tmux ←"}},   {key: ALT, popup: {macro: "CTRL f TAB", display: "tmux →"}},   {key: TAB, popup: {macro: "ALT a", display: A-a}},   {key: LEFT, popup: HOME},   {key: DOWN, popup: PGDN},   {key: UP, popup: PGUP},   {key: RIGHT, popup: END},   {macro: "ALT j", display: A-j, popup: {macro: "ALT g", display: A-g}},   {key: KEYBOARD, popup: {macro: "CTRL d", display: exit}} ]]
"""
	file.write(sc)
	file.close()
	loading("[•] Refreshing ...")
	print ("————————————————————————")
	os.system("mv termux.properties /$HOME/.termux && termux-reload-settings")
	print ("[%s] done ... " % (time.strftime("%x")))
	print ("[%s] please restart termux app!" % (time.strftime("%x")))
	back = input("[%s] back " % (time.strftime("%x")))
	menu()



menu()
