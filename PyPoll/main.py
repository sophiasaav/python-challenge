#PyPoll
#dependencies
import os
import csv

#speficication
csvpath = os.path.join('/Users/sophiasaavedra/Desktop/ucb ext data analytics/python homework/python-challenge/PyPoll/resources/election_data.csv')
 
#count total votes
votes = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
        votes.append(row)
total_votes = len(votes)

#complete list of candidates who received votes
#names_list = []
#with open(csvpath) as csvfile:
#    csvreader = csv.reader(csvfile, delimiter = ',')
#    next(csvreader)
#    for name in csvreader:
#        name_col = name[2]
#        name1 = name_col
#        names_list.append(name1)

names_list = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for col in csvreader:
        names_list.append(col[2])
        
#return unique values of names_list
setname = set(names_list)
newlist = list(setname)

#total number of votes each candidate won & percentage of votes each candidate won



votes0 = names_list.count(newlist[0])
percent0 = int((votes0 / total_votes) * 100)
votes1 = names_list.count(newlist[1])
percent1 = int((votes1 / total_votes) * 100)
votes2 = names_list.count(newlist[2])
percent2 = int((votes2 / total_votes) * 100)

votes = [votes0, votes1, votes2]
percentages = [percent0, percent1, percent2]
winner_names = [newlist[0], newlist[1], newlist[2]]
#winner of the election based on popular vote
winner_votes = max(votes)
winner_votes_index = int(votes.index(winner_votes))
#print(winner_votes_index)
#votes(winner_votes_index)
and_the_winner_is = winner_names[winner_votes_index]

#printing results
print('Election Results')
print('------------------------------------------------------------------')
print('Total Votes:', total_votes)
print('------------------------------------------------------------------')
print(newlist[0], '{}%'.format(percent0), '({})'.format(votes0))
print(newlist[1], '{}%'.format(percent1), '({})'.format(votes1))
print(newlist[2], '{}%'.format(percent2), '({})'.format(votes2))
print('------------------------------------------------------------------')
print('Winner:', and_the_winner_is)
print('------------------------------------------------------------------')

#exporting text file with results
import os.path
my_path = '/Users/sophiasaavedra/Desktop/ucb ext data analytics/python homework/python-challenge/PyPoll/analysis/'
completeName = os.path.join(my_path, 'pybankanalysis' + ".txt" )
with open(completeName, 'w') as pypollanalysistxt:

    pypollanalysistxt.write('Election Results \n' + '------------------------------------------------------------------ \n' + 'Total Votes:' + ' ' + str(total_votes) + '\n' + '------------------------------------------------------------------' + '\n' + str(newlist[0]) + ' ' + '{}%'.format(str(percent0)) + ' ' + '({})'.format(str(votes0)) + '\n' + str(newlist[1]) + ' ' + '{}%'.format(str(percent1)) + ' ' + '({})'.format(str(votes1)) + '\n' + str(newlist[2]) + ' ' + '{}%'.format(str(percent2)) + ' ' + '({})'.format(str(votes2)) + '\n' + '------------------------------------------------------------------ \n' + 'Winner:' + ' ' + and_the_winner_is + '\n' + '------------------------------------------------------------------')
pypollanalysistxt.close()
