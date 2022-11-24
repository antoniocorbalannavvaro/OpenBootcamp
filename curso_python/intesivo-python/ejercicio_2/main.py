from diary_class import Diary
from functions import *
from variables import show_options, show_header

def __main__():
    
    diary = Diary()
    #Dummie data:
    diary.add_contact('pepe', 64573459 )
    diary.add_contact('pedro', 623485964)
    diary.add_contact('antonio', 667788460)
    diary.add_contact('andrea', 613452375)
    diary.add_contact('maria', 667323201 )
    diary.add_contact('marta', 60234567 )
    diary.add_contact('lucas', 600123456)
    diary.add_contact('lucia', 639601254 )


    show_header()
    
    while True:
        
        show_options()
    
        options = input('Chose option: ')
        
        try:
            options = int(options)
        
        except:
            pass

        match options:
            case 0:
                print('Thanks for using my diary!\nGoodbye :)')
                break

            case 1: 
                case_add_user(diary)

            case 2:
                case_delete_user(diary)
                
            case 3:
               case_search_contact(diary)
                        
            case 4:
               case_get_phone(diary)
                
            case 5:
                case_show_contacts(diary)
                
            case _:
                print("Invalid option\nChoose a number between 0 and 5")

__main__()