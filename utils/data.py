import labor
import drugs 

labor_list = labor.get_results()
drug_list = drugs.get_reports()

#print labor_list[1]
def pop(iter):
	return drug_list[iter]["Population"]["26+"] + drug_list[iter]["Population"]["18-25"]
def getDrugRates(iter):
	return drug_list[iter]["Rates"]["Illicit Drugs"]["Abuse Past Month"]["26+"] + drug_list[iter]["Rates"]["Illicit Drugs"]["Abuse Past Month"]["18-25"]
def getPainRates(iter):
	return drug_list[iter]["Rates"]["Pain Relievers Abuse Past Year"]["26+"] + drug_list[iter]["Rates"]["Pain Relievers Abuse Past Year"]["18-25"]
def getAlcoholRates(iter):
	return drug_list[iter]["Rates"]["Alcohol"]["Abuse Past Year"]["26+"] + drug_list[iter]["Rates"]["Alcohol"]["Abuse Past Year"]["18-25"]


drug_list = drugs.get_reports()
print drug_list[1]["State"]

def OneYearDrugRates(i):
	totalpop = 0
	totalrate = 0
	start = 50* (i -1)
	end = 50*i + 1
	for num in range(start,end):
		totalrate += (getDrugRates(num)/100.0) * pop(num)
		totalpop += pop(num)
	totalrate = round(totalrate)
	rate = totalrate/totalpop
	return round(rate * 100, 2)

def OneYearPainRates(i):
	totalpop = 0
	totalrate = 0
	start = 50* (i -1)
	end = 50*i + 1
	for num in range(start,end):
		totalrate += (getPainRates(num)/100.0) * pop(num)
		totalpop += pop(num)
	totalrate = round(totalrate)
	rate = totalrate/totalpop
	return round(rate * 100, 2)

def OneYearAlcoholRates(i):
	totalpop = 0
	totalrate = 0
	start = 50* (i -1)
	end = 50*i + 1
	for num in range(start,end):
		totalrate += (getAlcoholRates(num)/100.0) * pop(num)
		totalpop += pop(num)
	totalrate = round(totalrate)
	rate = totalrate/totalpop
	return round(rate * 100, 2)

def makeDrugList():
	list = []
	for i in range(1,14):
		list.append(OneYearDrugRates(i))
	return list

def makePainList():
	list = []
	for i in range(1,14):
		list.append(OneYearPainRates(i))
	return list

def makeAlcoholList():
	list = []
	for i in range(1,14):
		list.append(OneYearAlcoholRates(i))
	return list

print makeDrugList()
print makePainList()
print makeAlcoholList()



