import os

# че смотришь копипастер



import colorama

import pystyle

from pystyle import Write, Colors



os.system('clear')



banner = '''

                  ██╗       ██╗██╗███╗  ██╗

                  ██║  ██╗  ██║██║████╗ ██║

                  ╚██╗████╗██╔╝██║██╔██╗██║

                   ████╔═████║ ██║██║╚████║

                   ╚██╔╝ ╚██╔╝ ██║██║ ╚███║

                    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝

               telegram channel > anhitable.t.me

███████████████████████████████████████████████████████████████

                                                            

                      [1] поиск по номеру                   

                      [2] поиск по IP                  

                      [3] поиск по нику                     

                      [4] поиск по БД                      

                      [5] поиск по GetContact              

                      [6] поиск по TG ID     

                      [99] выход                   

                    

███████████████████████████████████████████████████████████████                           

'''



Write.Print(banner, Colors.blue_to_white, interval=0.0001)



print(" ")



choice = input("ввод: ")



if choice == '1':

   print("временно не доступно")



elif choice == '2':

     from ip import ip



elif choice == '3':

     from nickname import nickname



elif choice == '4':

     from bd import bd



elif choice == '5':

     from getcontact import getcontact



elif choice == '6':

     from tg import tg





elif choice == '99':

     exit()
