import os
import phonenumbers
from phonenumbers import geocoder,carrier,timezone
from colorama import init
from termcolor import colored


def banner():
    os.system("clear")
    init()
    print(colored("""
______ _                           ______      _   
| ___ \ |                          |  _  \    | |  
| |_/ / |__   ___  _ __   ___ _ __ | | | |___ | |_ 
|  __/| '_ \ / _ \| '_ \ / _ \ '_ \| | | / _ \| __|
| |   | | | | (_) | | | |  __/ | | | |/ / (_) | |_ 
\_|   |_| |_|\___/|_| |_|\___|_| |_|___/ \___/ \__|""","red"))

    print(colored("""
coder By Rei-ken
Github   : https://github.com/Rei-ken/
Youtube  : https://youtube.com/channel/UC0huPBEXz8EW8SekJWVE_JQ
Discord  : https://discord.gg/fMWyY5b
Web Site : https://reiken.online/""","cyan"))
def phone_info():
    while True:
        init()
        print("1]çıkış / Exit")
        print("2]Telefon No. Bilgi topla /Phone Number in İnformation")
        i=input("----->")
        def operation():
            if (i=="1"): 
                exit()
            elif(i=="2"):
                banner()
                number=input(colored("Telefon Numarasını ülke kodu ile birlikte giriniz-enter your phone number with country code (+90..........): ","green"))
                phone_number = phonenumbers.parse(number, None)  
                print("Ülke/Şehir-Country/City: ",geocoder.description_for_number(phone_number,'tr'))
                print("Saat dilimi-Time zone: ",timezone.time_zones_for_number(phone_number))
                print("Operatör-Operator: ",carrier.name_for_number(phone_number,'tr')) 
            else: 
                print("Hatalı işlem-Incorrect operation")
        operation()
banner()
phone_info()

