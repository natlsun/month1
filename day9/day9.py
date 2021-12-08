#0

d= {3,10,11,13,31,21,1,10,3,5,6,6}
d.discard(7)
print(d)
#1
f= {"dog", "cat", "mouse", "sheep"}
f1={"cow", "horse", "donkey", "cat", "dog"}
f.intersection(f1)
print(f)
#2
f3= {"cow", "horse", "donkey", "cat", "dog"}
f2 = {"dog", "cat", "mouse", "sheep"}
f3.difference(f)
print(f3)

#3
a={1, 1.2,"wer", False,(1,2,3)}
a.add(1)
a.pop()
print(a)

#000

menu = {'lagman': 120, 
'plov': '120',
 'borsh': 100}
menu.update({'beshbarmak': 130})
menu['lagman']=135
menu.pop('borsh')
print(menu)
 #10
menu = {'lagman': 120, 
'plov': '120',
 'borsh': 100}
menu.update({'drinks': ['Coca-Cola','sprite','Fanta']})
print(menu)
#020
a={'.add() , .update(), .differens() , .remove(), .clear(), .discard(), .pop(), .intersection() ,'}
b={'.clear(), .keys() , .get() , values() , .update() , .items() '}
a.intersection_update(b)
print(a)
# 31
#a=()
#b=input("введите имя")
#for i in range(b): 
#	print(b and i)
#27
a={'nursultan': ['programist'],
'aijan': ['doctor']
}
	print(a)

