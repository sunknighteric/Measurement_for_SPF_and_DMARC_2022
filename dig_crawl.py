import os

if 0:
	f = open("./top.csv", "r")
	l = f.readlines()
	f.close()
	f = open("test.csv", "w")
	newl = []
	for i in l:
		var = i.split(".")
		newl.append(str(var[len(var)-2].strip(" ").strip("\n"))+"."+str(var[len(var)-1]).strip(" ").strip("\n"))
	print(len(newl))
	print(newl[0], newl[1])
	ll = list(set(newl))
	print(len(ll))
	for i in ll:
		f.write(i+"\n")
	f.close()


if 0:
	f = open("./mx_re_list.txt", "r")
	count_1 = 0
	count_2 = 0
	l = f.readlines()
	f.close()
	print(len(l))
	f = open("./mxre.csv", "w+")
	for k in l:
		if os.popen("dig +short MX " + k).readline().find(k) < 0:
			f.write(k + " no" +"\n")
			count_1 = count_1 + 1
			print(0)
			print(count_1+count_2)
		else:
			f.write(k + " yes" +"\n")
			count_2 = count_2 + 1
			print(k)
			print(count_1+count_2)
	f.close()
	print("mxdone")
	#print(count_2+count_1)
if 0:
	f = open("./spf_re_list.txt", "r")
	count_1 = 0
	count_2 = 0
	l = f.readlines()
	f.close()
	print(len(l))
	f = open("./spfre.csv", "w+")
	for k in l:
		var = os.popen("dig +short TXT " + k).readlines()
		if  len(var) == 0:
			f.write(k + ";no" +"\n")
			count_1 = count_1 + 1
			print(count_1+count_2)
			#print("spf")
		else:
			spf = ""
			for i in var:
				if i.find("\"v=") >= 0 or i.find("\"=spf") >= 0:
					spf = i
					break
			if spf == "":
				f.write(k + ";no" +"\n")
				count_1 = count_1 + 1
			else:	
				f.write(k + ";" + spf.replace("\n","") + "\n")
				count_2 = count_2 + 1
			print(count_1+count_2)
	
	print("spfredone")
	print(count_2)
	f.close()

if 0:
	f = open("./dmarc_re.txt", "r")
	count_1 = 0
	count_2 = 0
	l = f.readlines()

	f.close()
	print(len(l))
	f = open("./dmarcre.csv", "w+")
	for k in l:
		var = os.popen("dig +short TXT _dmarc." + k).readline()
		if  var == "":
			f.write(k + ";no" +"\n")
			count_1 = count_1 + 1
			print(count_1+count_2)
		else:
			f.write(k + ";" + var.replace("\n","") + "\n")
			count_2 = count_2 + 1
			print(count_1+count_2)
	print(count_1)
	print(count_2)
	print("dm redone")
	f.close()

if 1:
	f = open("./spfsub_re_list.txt", "r")
	count_1 = 0
	count_2 = 0
	#l = f.readlines()[55000:133000]
	l = f.readlines()
	f.close()
	print(len(l))
	f = open("./spfsubre.csv", "w+")
	for k in l:
		var = os.popen("dig +short TXT *." + k).readlines()
		if  len(var) == 0:
			f.write(k + ";no" +"\n")
			count_1 = count_1 + 1
			print(count_1+count_2)
		else:
			spf = ""
			for i in var:
				if i.find("\"v=") >= 0 or i.find("\"=spf") >= 0:
					spf = i
					break
			if spf == "":
				f.write(k + ";no" +"\n")
				count_1 = count_1 + 1
			else:	
				f.write(k + ";" + spf.replace("\n","") + "\n")
				count_2 = count_2 + 1
				print("sub")
	
	print(count_1)
	print("finish spfsubre")
	f.close()
