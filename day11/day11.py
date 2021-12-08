

#1
#dir=' bin    dev   lib    libx32      mnt   root  snap      sys  var
#boot   etc   lib32  lost+found  opt   run   srv       tmp
#cdrom  home  lib64  media       proc  sbin  swapfile  usr
#'''
#with open("nbas.txt",'w') as f:
#	f.write(dir)
#with open("nbas.txt",'r') as ff:
#	print(ff.read())

#2
#i=input("введите логин:")
#with open('nba.txt' , 'a') as f:
#	f.write(i)
#with open('nba.txt','r')as ff:
#	print(ff.read())
#a=input("введите пароль:")
#with open('nba.txt' , 'a') as l:
#	l.write(a)
#with open('nba.txt' , 'r') as ll:
#	print(ll.read())
#3
#with open('nba.txt' , 'r') as l:
#	if "w" in l.read():
#		print("да, в тексте есть w")
#	else:
#		print("нет, в тексте нет w")
#4
#t_words=[]
#with open('kier.txt', 'r') as f:
#	for i in f.read().split():
#		if "T" in i or "t" in i:
#			t_words.append(i)
#		else:
#
#			print("err")
#print(t_words)

#5
#log=input("введите логин")
#pasww=input("введите пароль")
#keylogger={'login': None, 'password' : None}
#ff=open("nba.txt", 'a')
#logg=keylogger["login"]=log
#passwww=keylogger["password"]=pasww
#ff.writelines("login : "+logg+"  "+"password: "+passwww+ "\n")
#ff.close()

#with open("nba.txt", "r") as f:
#	print(f.read())
a=input("введите логин")
b=input("введите пароль")
c=input("покажите фото")
with open("nba.txt" , "r") as l:
	if 'jpeg' or 'jpg' or 'png' in c.read():
		print("регистрация успешна")
	else:
		print("нету такой расшерении")
