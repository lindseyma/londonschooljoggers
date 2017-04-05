import labor
import drugs 
from collections import OrderedDict

labor_list = labor.get_results()
drug_list = drugs.get_reports()

#print labor_list[1]["Data"]["Civilian Noninstitutional Population"]

def pop(iter):
	return drug_list[iter]["Population"]["26+"] + drug_list[iter]["Population"]["18-25"]
def getDrugRates(iter):
	return drug_list[iter]["Rates"]["Illicit Drugs"]["Abuse Past Month"]["26+"] + drug_list[iter]["Rates"]["Illicit Drugs"]["Abuse Past Month"]["18-25"]
def getPainRates(iter):
	return drug_list[iter]["Rates"]["Pain Relievers Abuse Past Year"]["26+"] + drug_list[iter]["Rates"]["Pain Relievers Abuse Past Year"]["18-25"]
def getAlcoholRates(iter):
	return drug_list[iter]["Rates"]["Alcohol"]["Abuse Past Year"]["26+"] + drug_list[iter]["Rates"]["Alcohol"]["Abuse Past Year"]["18-25"]
def getMarijuanaRates(iter):
	return drug_list[iter]["Rates"]["Marijuana"]["Used Past Month"]["26+"] + drug_list[iter]["Rates"]["Marijuana"]["Used Past Month"]["18-25"]
def getCocaineRates(iter):
	return drug_list[iter]["Rates"]["Illicit Drugs"]["Cocaine Used Past Year"]["26+"] + drug_list[iter]["Rates"]["Illicit Drugs"]["Cocaine Used Past Year"]["18-25"]
def getTobaccoates(iter):
	return drug_list[iter]["Rates"]["Tobacco"]["Use Past Month"]["26+"] + drug_list[iter]["Rates"]["Tobacco"]["Use Past Month"]["18-25"]

drug_list = drugs.get_reports()
#print drug_list[1]

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

def OneYearMarijuanaRates(i):
	totalpop = 0
	totalrate = 0
	start = 50* (i -1)
	end = 50*i + 1
	for num in range(start,end):
		totalrate += (getMarijuanaRates(num)/100.0) * pop(num)
		totalpop += pop(num)
	totalrate = round(totalrate)
	rate = totalrate/totalpop
	return round(rate * 100, 2)

def OneYearCocaineRates(i):
	totalpop = 0
	totalrate = 0
	start = 50* (i -1)
	end = 50*i + 1
	for num in range(start,end):
		totalrate += (getCocaineRates(num)/100.0) * pop(num)
		totalpop += pop(num)
	totalrate = round(totalrate)
	rate = totalrate/totalpop
	return round(rate * 100, 2)

def OneYearTobaccoates(i):
	totalpop = 0
	totalrate = 0
	start = 50* (i -1)
	end = 50*i + 1
	for num in range(start,end):
		totalrate += (getTobaccoRates(num)/100.0) * pop(num)
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

def makeMarijuanaList():
	list = []
	for i in range(1,14):
		list.append(OneYearMarijuanaRates(i))
	return list
def makeCocaineList():
	list = []
	for i in range(1,14):
		list.append(OneYearCocaineRates(i))
	return list
def makeTobaccoist():
	list = []
	for i in range(1,14):
		list.append(OneYearTobaccoRates(i))
	return list
#labor
#print labor_list[1]

'''print makeDrugList()
print makePainList()
print makeAlcoholList()'''

#only find employment rates
def population(iter):
	return labor_list[iter]["Data"]["Civilian Noninstitutional Population"]["White"] + labor_list[iter]["Data"]["Civilian Noninstitutional Population"]["Black or African American"]

def getWhiteRates(iter):
	return labor_list[iter]["Data"]["Employed"]["White"]["Counts"]["All"]

def getAfAmRates(iter):
	return labor_list[iter]["Data"]["Employed"]["Black or African American"]["Counts"]["All"]

def OneYearEmployedRates(i):
	a = (getWhiteRates((i-1972)*12) + getAfAmRates((i-1972)*12))
	b = (population(i-1972)*12)
	return (a/b)*1000

def OneYearUnemployedRates(i):
	return 100 - OneYearEmployedRates(i)

def OneYearDict(i):
	return OrderedDict([("Year",i), (("Employed"), OneYearEmployedRates(i)), (("Unemployed"), OneYearUnemployedRates(i))])

def makeLaborList():
	list=[]
	for i in range(2002,2015):
		list.append(OneYearDict(i))
	return list

#print(population(1))
l =  makeLaborList()
for labor in l:
        print labor.keys()

d = makeAlcoholList()
for drug in d:
       print drug
