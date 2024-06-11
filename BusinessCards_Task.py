from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self,name,surname,telephone,email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f'{self.name} | {self.surname} | {self.telephone} | {self.email}'
    
    def contact(self):
        print ('Wybieram numer ' + str(self.telephone) + ' i dzwonię do ' + str(self.name) + ' ' + str(self.surname))
        return '----------'

    @property
    def label_lenght(self):
        self.lenght = len(self.name) + 1 + len(self.surname)
        return self.lenght

class BusinessContact(BaseContact):
    def __init__(self, position, company, workTelephone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.workTelephone = workTelephone

    def __str__(self):
        return f'{self.name} | {self.surname} | {self.position} | {self.company} | {self.workTelephone} | {self.email}'

    def contact(self):
        print ('Wybieram numer służbowy ' + str(self.workTelephone) + ' i dzwonię do ' + str(self.name) + ' ' + str(self.surname))    
        return '----------'

    @property
    def label_lenght(self):
        self.lenght = len(self.name) + 1 + len(self.surname)
        return self.lenght

while True:
    try:
        cardType = int(input('Proszę podać rodzaj kontaktu, wybierając cyfrę - 1.Zwykły, 2.Biznesowy'))
        if cardType < 1 or cardType > 2:
            print('Proszę podać cyfrę 1 lub 2')
            continue
        else:
            break
    except:
        print('Proszę podać cyfrę')
        continue

while True:
    try:
        cardQuantity = int(input('Proszę podać ilość osób do wygenerowania'))
        break
    except:
        print('Proszę podać liczbę całkowitą')
        continue

def create_contacts(cardType,cardQuantity):

    for i in range(0,cardQuantity):
        if cardType == 1:
            basePerson = BaseContact(name=fake.name(),surname=fake.last_name(),telephone=fake.phone_number(),email=fake.email())
            print(basePerson)
            print(basePerson.contact())

        elif cardType == 2:
            businessPerson = BusinessContact(name=fake.name(),surname=fake.last_name(),telephone=fake.phone_number(),position=fake.job(),company=fake.company(),workTelephone=fake.phone_number(),email=fake.email())
            print(businessPerson)
            print(businessPerson.contact())

    return

create_contacts(cardType,cardQuantity)

