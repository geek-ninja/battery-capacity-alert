#Battery status notification for linux(Kali linux)
import os
import pyautogui

#Change the dir to the battery status location of your OS.
#os.chdir('../') use this line to change the dir to root or ignore if you are running this program in root. 
os.chdir('/sys/class/power_supply/BAT0')# this dir may be different in different os.

try:
    while(1):
        print('Press ctrl + c to stop the program')
        status = open('status','r').readline().strip()
        if status == 'Charging':
            power = open('capacity','r').readline().strip()
            print('Battery Status :'+status)
            print('Current Charge is :'+power+'%')
            power = int(power)
            if power == 90:
                print('╔══════════════════════╗  ')
                print('║╔════════════════════╗╚╗ ')
                print('║║██████████████████  ╚╗╚╗')
                print('║║███████   90%  ████ ─║║║')
                print('║║██████████████████  ╔╝╔╝')
                print('║╚════════════════════╝╔╝ ')
                print('╚══════════════════════╝  ')
                
                notification = 'Battery capacity is now '+str(power)+'%'
                pyautogui.alert(notification)
                pyautogui.alert('Turn off the charger')
            elif power == 95:
                print('╔══════════════════════╗  ')
                print('║╔════════════════════╗╚╗ ')
                print('║║██████████████████  ╚╗╚╗')
                print('║║███████   95%  ████ ─║║║')
                print('║║██████████████████  ╔╝╔╝')
                print('║╚════════════════════╝╔╝ ')
                print('╚══════════════════════╝  ')

                notification = 'Battery capacity is now '+str(power)+'%'
                pyautogui.alert(notification)
                pyautogui.alert('Turn off the charger')
        elif status == 'Discharging':
            power = open('capacity','r').readline().strip()
            print('Battery Status :'+status)
            print('Current Charge is :'+power+'%')
            power = int(power)
            if power == 10:
                print('╔══════════════════════╗  ')
                print('║╔════════════════════╗╚╗ ')
                print('║║█████████           ╚╗╚╗')
                print('║║███████   10%       ─║║║')
                print('║║█████████           ╔╝╔╝')
                print('║╚════════════════════╝╔╝ ')
                print('╚══════════════════════╝  ')

                notification = 'Battery capacity is now '+str(power)+'%'
                pyautogui.alert(notification)
                pyautogui.alert('Turn on your charger')
            elif power == 5:
                print('╔══════════════════════╗  ')
                print('║╔════════════════════╗╚╗ ')
                print('║║██                  ╚╗╚╗')
                print('║║███████    5%       ─║║║')
                print('║║██                  ╔╝╔╝')
                print('║╚════════════════════╝╔╝ ')
                print('╚══════════════════════╝  ')

                notification = 'Battery capacity is now '+str(power)+'%'
                pyautogui.alert(notification)
                pyautogui.alert('Turn on your charger')
                
except:
    print('\nprogram is stopped ')
    print('or')
    print('please check your battery files location !')
