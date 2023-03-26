#PyBank Challenge
#dependencies
import os
import csv

#speficication
csvpath = os.path.join('/Users/sophiasaavedra/Desktop/ucb ext data analytics/python homework/python-challenge/PyBank/resources/budget_data.csv')
 
#count total months
months = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
        months.append(row)
total_months = len(months)

#count net total amount of "Profit/Losses"
profit_col = []
profit_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #skip first row
    next(csvreader)
    for row in csvreader:
        #selecting column
        profit_col = row[1]
        int1 = int(profit_col)
        profit_list.append(int1)
net_profit = sum(profit_list)

#calculating the avg changes in "Profit/Losses"
from statistics import mean
delta_list = []

alist = profit_list[0:total_months - 1]
blist = profit_list[1:total_months]

zipped = zip(alist, blist)
for a, b in zipped:
    delta_list.append(b - a)
avg_change = int(mean(delta_list))

#calculating the greatest increase in profits (date and amount) over the entire period
inc_profit = max(delta_list)

#locating the month associated with this increase
inc_profit_index = months[(int(delta_list.index(inc_profit)) + 1)]
inc_profit_month = inc_profit_index[0]

#calculating the greatest decrease in profits (date and amount) over the entire period
dec_profit = min(delta_list)
#locating the month associated with this decrease
dec_profit_index = months[(int(delta_list.index(dec_profit)) + 1)]
dec_profit_month = dec_profit_index[0]

#printing results
print('Financial Analysis')
print('------------------------------------------------------------------')
print('Total Months:', total_months)
print('Net Profit:', '${}'.format(net_profit))
print('Average Change:', '${}'.format(avg_change))
print('Greatest Increase in Profits:', inc_profit_month, '${}'.format(inc_profit))
print('Greatest Decrease in Profits:', dec_profit_month, '${}'.format(dec_profit))

#exporting text file with results
import os.path
my_path = '/Users/sophiasaavedra/Desktop/ucb ext data analytics/python homework/python-challenge/PyBank/analysis'
completeName = os.path.join(my_path, 'pybankanalysis' + ".txt" )
with open(completeName, 'w') as pybankanalysistxt:
    pybankanalysistxt.write('Financial Analysis \n' + '------------------------------------------------------------------ \n' + 'Total Months: ' + str(total_months) + '\n' + 'Net Profit: ' + '${}'.format(str(net_profit)) + '\n' + 'Average Change: ' + '${}'.format(str(avg_change)) + '\n' + 'Greatest Increase in Profits: ' + str(inc_profit_month) + ' ' + '${}'.format(str(inc_profit)) + '\n' + 'Greatest Decrease in Profits: ' + str(dec_profit_month) + ' ' + '${}'.format(str(dec_profit)))
    pybankanalysistxt.close()
