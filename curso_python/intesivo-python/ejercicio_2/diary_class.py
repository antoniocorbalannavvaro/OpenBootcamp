import functools;

def add_contact_exception(call):
    @functools.wraps(call)
    def catch_error(*args, **kwargs):
        try:
            return call(*args, **kwargs)
        
        except Exception as e:
            print (f'Invalid params for method "{call.__name__}"')
            
    return catch_error

class Diary:
    
    contacts = [] 
    
    @add_contact_exception
    def add_contact(self, name, phone):
        new_contact = {name.upper():phone}
        self.contacts.append(new_contact)
 
    def delete_contact(self, name):
        for i in self.contacts:
            if (list(i.keys())[0]) == name:
                del i[name]
            else:
                pass
            
        self.contacts = list(filter(None, self.contacts))

                
    def get_phone(self, name):
        for i in self.contacts:
            if (list(i.keys())[0]) == name:
                return i[name]

    def show_contacts(self):
        return self.contacts
        
    def search_contact(self, search):
        search = search.upper()
        matches = []
        for i in self.contacts:
            if (list(i.keys())[0]).startswith(search):
                matches.append(i)

        return matches