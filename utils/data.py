import labor
import drugs 

labor_list = labor.get_results()
#print labor_list[1]

drug_list = drugs.get_reports()
print drug_list[50]["State"]