

#mx_record_process
if 0:
	f = open("./mx_no.txt", "r")
	l = f.readlines()
	print("MX Statistic")
	print(len(l))
	f.close()
	count1 = 0
	count2 = 0
	count3 = 0
	f2 = open("./mx_re_list.txt", "w")
	f1 = open("./mx_no.csv", "w+")
	for i in l:
		name = i[i.find("name") + 7:i.find("status")-3]	
		status = i[i.find("status") + 9:i.find("timestamp")-3]
		if i.find("\"type\":\"MX\"") >= 0:
			count1 = count1 + 1
			f1.write(name + ",yes\n")
			continue	
		elif i.find("SERVFAIL") >= 0 or i.find("TIMEOUT") >=0 :
			#name = i[i.find("name") + 7:i.find("status")-3]
			f2.write(name + "\n")
			count2 = count2 + 1
		else:
			f1.write(name + ",no\n")
			count3 = count3 + 1
	print(count1, count2, count3)
	f1.close()
	f2.close()
#spf_record_process
if 0:
	f = open("./spf_no.txt", "r")
	print("SPF Statistic")
	l = f.readlines()
	print(l[0])
	count1 = 0
	count2 = 0
	count3 = 0
	f.close()
	f2 = open("./spf_re_list.txt", "w")
	re = []
	if 1:
		f1 = open("./spf_no.csv", "w+")
		f1.write("name,status,spf\n")
		for i in l:
			s = ""
			status = i[i.find("status") + 9:i.find("timestamp")-3]
			name = i[i.find("name") + 7:i.find("status")-3]
			if i.find("SERVFAIL") >= 0 or i.find("TIMEOUT") >=0 :
			#name = i[i.find("name") + 7:i.find("status")-3]
				re.append(name)
				count3 = count3 + 1	
				continue		
			if i.find("spf") > 0:
				spf = i[i.find("spf") + 6 : i.find("name") - 4]
				if spf.find("\"") >=0 or name.find("\"") >=0 :
					re.append(name.split("\"")[-1].strip("\n"))
					count3 = count3 + 1	
					continue		
				count1 = count1 + 1
			else:
				spf = "--"
				status = ""
				count2 = count2 + 1
			s = name + "," + status + "," + spf
			f1.write(s+ "\n")
		f1.close()
	re = list(set(re))
	for i in re:
		f2.write(i+"\n")
	f2.close()
	print(count1, count2, count3)


#spf_sub_record_process
if 1:
	f = open("./spfsub_no.txt", "r")
	print("SPFsub Statistic")
	l = f.readlines()
	print(l[0])
	count1 = 0
	count2 = 0
	count3 = 0
	f.close()
	f2 = open("./spfsub_re_list.txt", "w")
	re = []
	if 1:
		f1 = open("./spfsub_no.csv", "w+")
		f1.write("name,status,spf\n")
		for i in l:
			s = ""
			status = i[i.find("status") + 9:i.find("timestamp")-3]
			name = i[i.find("\"name\"") + 7:i.find("\"status\"")-2].replace("\"","")
			print(name)
			if i.find("SERVFAIL") >= 0 or i.find("TIMEOUT") >=0 :
			#name = i[i.find("name") + 7:i.find("status")-3]
				re.append(name)
				count3 = count3 + 1	
				continue		
			if i.find("\"spf\"") >= 0:
				spf = i[(i.find("\"spf\"") + 7) : (i.find("\"name\"") - 3)]
				#print(spf)
				if spf.find("\"") >=0 or name.find("\"") >=0 :
					re.append(name.split("\"")[-1].strip("\n").replace("*.", ""))
					count3 = count3 + 1	
					continue		
				count1 = count1 + 1
			else:
				spf = "--"
				status = ""
				count2 = count2 + 1
			s = name + "," + status + "," + spf
			f1.write(s+ "\n")
		f1.close()
	re = list(set(re))
	for i in re:
		f2.write(i+"\n")
	f2.close()
	print(count1, count2, count3)

#spf_seperate_record_process
if 0:
	f1 = open("./spf_record.csv", "w+")
	f1.write("name,status,spf\n")	
	f = open("./test_1/spf_test.txt", "r")
	print("SPF Statistic")
	l = f.readlines()
	print(l[0])
	count1 = 0
	count2 = 0
	f.close()
	if 1:
		
		for i in l:
			if i[i.find("}")-1] == "{":
				spf = ""
				count2 = count2 + 1
			else:			
				name = i[i.find("name") + 7:i.find("status")-3]
				spf = i[i.find("spf") + 6 : i.find("name") - 4]
				count1 = count1 + 1
				
			s = name + "," + status + "," + spf
			f1.write(s+ "\n")
		f1.close()
	print(count1, count2)

#dmarc_record_process
if 0:
	f = open("./dmarc_no.txt", "r")
	l = f.readlines()
	print(len(l))
	count3 = 0
	f.close()
	name = l[0][l[0].find("\"name\"") + 8:l[0].find("\"status\"")-2]
	data = l[0][(l[0].find("\"data\"") + 17):(l[0].find("\"name\"")-3)]
	print(name)
	print(data)
	f2 = open("./dmarc_re.txt", "w+")
	if 1:
		f1 = open("./dmarc_no.csv", "w+")
		f1.write("name,status,dmarc\n")
		for i in l:
			s = ""
			name = i[(i.find("\"name\"") + 8):(i.find("\"status\"")-2)]
			data = i[(i.find("\"data\"") + 17):(i.find("\"name\"")-3)]
			status = ""
			if i.find("SERVFAIL") >= 0 or i.find("TIMEOUT") >=0 :
			#name = i[i.find("name") + 7:i.find("status")-3]
				f2.write(name+"\n")
				count3 = count3 + 1	
				continue		
			#if i.find("dmarc") > 0:
			#	spf = i[i.find("dmarc") + 6 : i.find("name") - 4]
			#else:
			#	spf = ""
			if data == "":
				status = "--"
			s = name + "," + status + "," + data
			f1.write(s+ "\n")
		f1.close()
	f2.close()
	print(count3)

#subdomain_spf
if 0:
	f = open("./spf_sub_500.txt", "r")
	l = f.readlines()
	print("spf subdomain Statistic")
	#print(len(l))
	f.close()

	count_ok = 0
	count_invalid = 0

	#define -all 1; ~all 2; ?all 3; +all 4; redirect 5; include 6
	count_1 = 0
	count_2 = 0
	count_3 = 0
	count_4 = 0
	count_5 = 0
	count_6 = 0

	for i in l:
		if i.find("*.") < 0:
			continue
		if i.find("-all")>= 0:
			count_1 = count_1 + 1
			count_ok = count_ok + 1
		elif i.find("~all")>= 0:
			count_2 = count_2 + 1
			count_ok = count_ok + 1
		elif i.find("?all")>= 0:
			count_3 = count_3 + 1
			count_ok = count_ok + 1
		elif i.find("+all")>= 0:
			count_4 = count_4 + 1
			count_ok = count_ok + 1
		elif i.find("redirect")>= 0:
			count_5 = count_5 + 1
			count_ok = count_ok + 1
		elif i.find("include")>= 0:
			count_6 = count_6 + 1
			count_ok = count_ok + 1
		else:
			if i.find("SERVFAIL") > 0 or i.find("TIMEOUT") > 0:
				name = i[i.find("name") + 7:i.find("status")-3]
				print(name)
				continue			
			count_invalid = count_invalid + 1
	print("ok:" + str(count_ok) + "  invalid  " + str(count_invalid) + "  " + str(count_ok+count_invalid) + "\n")
	print("OK type\n-:" + str(count_1) + "  ~:" + str(count_2) + "  ?:" + str(count_3) + "  +:" + str(count_4) +"  redirect:" + str(count_5) +"  include:" + str(count_6) + "\n")


#statisitic
#dmarc_subdomain_process
if 0:
	f = open("./dmarc_500.txt", "r")
	l = f.readlines()
	print("dmarc subdomain Statistic")
	f.close()
	count_ok = 0
	count_invalid = 0

	#define none 1; quarantine 2; reject 3
	count_1 = 0
	count_2 = 0
	count_3 = 0
	for i in l:
		if i.find("sp=") > 0:
				count_ok = count_ok + 1
				if i.find("sp=reject") > 0:
					count_3 = count_3 + 1
				elif i.find("sp=quarantine") > 0:
					count_2 = count_2 + 1
				elif i.find("sp=none") > 0:
					count_1 = count_1 + 1
				else:
					count_invalid = count_invalid + 1
		else:
			if i.find("SERVFAIL") > 0 or i.find("TIMEOUT") > 0:
				name = i[i.find("name") + 7:i.find("status")-3]
				print(name)
				continue
			count_invalid = count_invalid + 1
	print("ok:" + str(count_ok) + "  invalid  " + str(count_invalid) + "  " + str(count_ok+count_invalid) + "\n")
	print("OK type\nnone:" + str(count_1) + "  quarantine:" + str(count_2) + "  reject:" + str(count_3) + "\n")


#spf_process
if 0:
	f = open("./spf_500.txt", "r")
	l = f.readlines()
	print("spf Statistic")
	print(len(l))
	f.close()

	count_ok = 0
	count_invalid = 0

	#define -all 1; ~all 2; ?all 3; +all 4; redirect 5; include 6
	count_1 = 0
	count_2 = 0
	count_3 = 0
	count_4 = 0
	count_5 = 0
	count_6 = 0

	for i in l:
		if i.find("-all")>= 0:
			count_1 = count_1 + 1
			count_ok = count_ok + 1
		elif i.find("~all")>= 0:
			count_2 = count_2 + 1
			count_ok = count_ok + 1
		elif i.find("?all")>= 0:
			count_3 = count_3 + 1
			count_ok = count_ok + 1
		elif i.find("+all")>= 0:
			count_4 = count_4 + 1
			count_ok = count_ok + 1
		elif i.find("redirect")>= 0:
			count_5 = count_5 + 1
			count_ok = count_ok + 1
		elif i.find("include")>= 0:
			count_6 = count_6 + 1
			count_ok = count_ok + 1
		else:
			if i.find("SERVFAIL") > 0 or i.find("TIMEOUT") > 0:
				name = i[i.find("name") + 7:i.find("status")-3]
				print(name)
				continue
			count_invalid = count_invalid + 1
	print("ok:" + str(count_ok) + "  invalid  " + str(count_invalid) + "  " + str(count_ok+count_invalid) + "\n")
	print("OK type\n-:" + str(count_1) + "  ~:" + str(count_2) + "  ?:" + str(count_3) + "  +:" + str(count_4) +"  redirect:" + str(count_5) +"  include:" + str(count_6) + "\n")
#dmarc_process
if 0:
	f = open("./dmarc_500.txt", "r")
	l = f.readlines()
	print("dmarc Statistic")
	print(len(l))
	f.close()

	count_ok = 0
	count_invalid = 0

	#define none 1; quarantine 2; reject 3
	count_1 = 0
	count_2 = 0
	count_3 = 0

	for i in l:
		if i.find("p=none") >= 0 :
			count_1 = count_1 + 1
			count_ok = count_ok + 1
		elif i.find("p=quarantine") >= 0:
			count_2 = count_2 + 1
			count_ok = count_ok + 1
		elif i.find("p=reject") >= 0 :
			count_3 = count_3 + 1
			count_ok = count_ok + 1
		else:
			if i.find("SERVFAIL") > 0 or i.find("TIMEOUT") > 0:
				name = i[i.find("name") + 7:i.find("status")-3]
				print(name)
				continue
			count_invalid = count_invalid + 1
	print("ok:" + str(count_ok) + "  invalid  " + str(count_invalid) + "  " + str(count_ok+count_invalid) + "\n")
	print("OK type\nnone:" + str(count_1) + "  quarantine:" + str(count_2) + "  reject:" + str(count_3) + "\n")
