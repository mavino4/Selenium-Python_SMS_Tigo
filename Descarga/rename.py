import os 
list = open('list.txt', 'r')
i = 1
for file in list:
	#print(file)
	os.system("mv captcha/%s New/%s.png" % (file[:-1],str(i)))
	i +=1 