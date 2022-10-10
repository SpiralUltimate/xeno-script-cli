from requests import get
from time import sleep
from os import system
from getpass import getpass
from Var import p
# this file is a cli for xeno script
version_current = "0.61"
def install(url_url, name):
    URL = url_url
    response = get(URL)
    open(name, "wb").write(response.content)
    print("file successfully installed")
def use(url, name):
    system(f"start {url}")
    print(f"{name} succesfully started")
# the code below is the main portion of code
def main_portion():
    while True:
        main_cli = input(f"hello {user} type a command to run ").lower()
        if main_cli in ("clear", "cls"):
            system("cls")
        if main_cli == "help":
            print("type cud to erase all user data in the user log file. type cls or clear to clear all commands excuted before the current line")
            print("type (xs modulename) to install a xs module")
        if main_cli == "q":
            quit()
        if main_cli == "cud":
            user_pass = getpass(prompt="type your password to continue ")
            if user_pass == password:
                f = open("user_log.txt", "w")
                f.write("")
                f.close()
            else:
                main_portion()
        if main_cli == "use xs-online":
            use("https://xeno-script-online.glitch.me", "xeno script online")
        if main_cli == "author":
            p("the author is Logan Keller")
        if main_cli in ("git pro", "git p", "p git"):
            use("https://github.com/SpiralUltimate?tab=repositories", "github repository page")
        if main_cli == "xs source.index":
            install('https://xeno-script-online.glitch.me/index.php', "index.html")
        if main_cli == "xs source":
            install("https://www.dropbox.com/s/c2p30guov7d8npu/xeno-script-online-2022-10-08_194344.tgz?dl=1", "xeno-script.tgz")
while True:
    version_url = "https://spiralultimate.github.io/xeno-script-cli/version.txt"
    version_get = get(version_url)
    version = version_get.content
    p(f"before opening this file check what version it is the latest version is {version} and the current version is {version_current} if the latest version is not the current version of this file please exit this file and run the update file")
    p("type a command to run. type help for more information")
    user = input("please enter your username ")
    password = getpass(prompt="please enter your password ")
    confirm = input(f"is password {password} and user {user} correct? ").lower()
    if confirm == "yes":
        p(".")
    if confirm == "no":
        print("the program is restarting...")
        continue
    confirm_log = input("do you want your password to be hashed in the user log file? please keep note if you do not want to store info in the userlog file please type dsd ").lower()
    if confirm_log == "yes":
        f = open("user_log.txt", "w")
        f.write(f"username is = {user} and password is = {len(password)}")
        f.close()
        main_portion()
    if confirm_log == "no":
        f = open("user_log.txt", "w")
        f.write(f"username is = {user} and password is = {password}")
        f.close()
        main_portion()
    if confirm_log == "dsd":
        with open("user_log.txt", "w") as f:
            f.write("")
        main_portion()
    else:
        continue
