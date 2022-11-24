
def case_add_user(diary):
    name = input("What's the name of the new contact?: ")
    name = name.upper()
    phone = input("What's the phone of the contact?: ")

    diary.add_contact(name, phone)
    print(f'Successfully!\n{name} with number {phone} is now in your diary.')


def case_delete_user(diary):
    name = input("What's the name of the contact you want to delete?: ")
    name = name.upper()
    phone = []
    
    for i in diary.show_contacts():
        if list(i.keys())[0] == name:
            phone.append(list(i.values())[0])
        else:
            pass
    
    if phone == []:
        print('User not found')
    
    else:
        diary.delete_contact(name)
        print(f'Successfully!\n{name} with number {phone[0]} was deleted.')

    
def case_search_contact(diary):
    name = input('Insert a name: ')
    name = name.upper()
    count = 1
    
    print('Users matches:')
    
    for i in diary.search_contact(name):
        print(f'{count}' + ')',list(i.keys())[0],
                list(i.values())[0])
        
        count += 1
        
  
def case_get_phone(diary):
    name = input('Insert a name: ')
    name = name.upper()

    if diary.get_phone(name) == None:
        print('User not found')
        
    else:
        print(f'{name} number:',diary.get_phone(name))
        

def case_show_contacts(diary):
    print('------- Users list -------')
    if len(diary.show_contacts()) < 1:
        print('Diary is empty')

    else:
        count = 1
        
        for i in diary.show_contacts():
            print(f'{count}' + ')', 'Name:',list(i.keys())[0],
                'Phone:',list(i.values())[0])
            count += 1
            