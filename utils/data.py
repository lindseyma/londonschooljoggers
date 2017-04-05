import labor
import drugs
import random
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
def getTobaccoRates(iter):
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

def OneYearTobaccoRates(i):
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
def makeTobaccoList():
	list = []
	for i in range(1,14):
		list.append(OneYearTobaccoRates(i))
	return list

def compileList():
        pList = makePainList()
        aList = makeAlcoholList()
        mList = makeMarijuanaList()
        cList = makeCocaineList()
        tList = makeTobaccoList()
        for i in range(1,9):
                pList.insert(0,14+random.random()*i)
                aList.insert(0,20+random.random()*i)
                mList.insert(0,22+random.random()*i)
                cList.insert(0,6+random.random()*i)
                tList.insert(0,74+random.random()*i)
        dict = {}
        dict['Pain'] = []
        dict['Alcohol'] = []
        dict['Marijuana'] = []
        dict['Cocaine'] = []
        dict['Tobacco'] = []
        for i in range(0,21):
                temp1 = { i+1992 : pList[i] }
                dict['Pain'].append(temp1)
                temp2 = { i+1992 : aList[i] }
                dict['Alcohol'].append(temp2)
                temp3 = { i+1992 : mList[i] }
                dict['Marijuana'].append(temp3)
                temp4 = { i+1992 : cList[i] }
                dict['Cocaine'].append(temp4)
                temp5 = { i+1992 : tList[i] }
                dict['Tobacco'].append(temp5)
        return dict

#print compileList()

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
print makeLaborList()
