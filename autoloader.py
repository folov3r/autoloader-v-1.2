# бета 1.1 // старался как мог над прогой, доводил до ума, буду дальше её доделывать, 
#в планах сделать запуск программ из определенной папки и усовершенствование скрипта стартапа
import os
import time
from colorama import init
from colorama import Fore, Back, Style
init()
clear = lambda: os.system('cls')
print (Fore.GREEN)
def console_picture():
    print("                                             //| |         |  =============  _______   ")
    print("                                            // | |         |       ||       /          ")
    print("                                           //  | |         |       ||      ||       || ")
    print("                                          //   |          /        ||      ||       || ")
    print("                                         //    |    _____/         ||        _______/  ")
    print("                                                                            LOADER.by folov3r   ")
console_picture()
print(Fore.RESET)
print("Проверка файла автозагрузки...")
if os.path.isfile("C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/start_autoloader.bat"):
    print("Файл загрузки существует")
else:
    my_file = open("C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/start_autoloader.bat", "w+")
    my_file.write("@echo off \n")
    my_file.write("start C:\\Users\\user\\Desktop\\autoloader\\autoloader.exe")
    my_file.close()
print(">>      Загрузка скрипта будет произведена через 5 сек для улучшении производительности \n")
time.sleep(5)
os.startfile('C:\\Users\\user\\Desktop\\autoloader\\programms.py')
clear()
print(">>      Программы запущены, спасибо за использование моей программы ) <3")
def console_picture():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("                                             //| |         |  =============  _______   ")
    print("                                            // | |         |       ||       /          ")
    print("                                           //  | |         |       ||      ||       || ")
    print("                                          //   |          /        ||      ||       || ")
    print("                                         //    |    _____/         ||        _______/  ")
    print("                                                                            LOADER.by folov3r   ")
console_picture()
time.sleep(30)
