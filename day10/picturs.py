
countries_of_east = ('Singapore', 'Malaysia', 'Indonesia', 'Hawaii')
user_order_0 = 'Brazil'
user_order_1 = 'Canada'
user_order_2 = 'Kyrgyzstan'
user_order_3 = 'Italy'
user_order_4 = 'Argentina'
user_order_5 = 'Malasia'
for east in countries_of_east:
    if user_order_2 in countries_of_east :
            print("Ваш рейс найден! Ваш класс ('эконом')")
            break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break
countries_of_east = ('Singapore', 'Malaysia', 'Indonesia', 'Hawaii')
client1 = input('куда вы летите в east?')
for east in countries_of_east:
    if client1 == east:
        print("Ваш рейс найден! Ваш класс (Business)")
        break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break
#2\
a={1,1,2,3,5,8,13,21,34,55,89}
b={1,2,3,4,5,6,7,8,9,10,11,12,13}
a.intersection_update(b)
print(a)
#3
a={

"Joomart": "+996555246810",
     "Adinai": "+996555013579",
     "Ermek": "+996777013579",
     "Atai": "+996777246810",
     "Aslan": "+996999246810",
} 
h = {
     "Lyazat": "+996551123456",
     "Salavat": "+996552234567",
     "Daniyar": "+996553345678",
     "Bolot": "+996554456789",
     "Alymbek": "+996555501234",
     "Dastan": "+996556678912",
     "Maksat": "+996557789012",
     "Aibek": "+996558890123",
}
a.update({"nursultan" : "+996707656558",})
b.update({"nursultan" : "+996707656558",})
a.update(b)
for  o in a:
	print(our_friends)
