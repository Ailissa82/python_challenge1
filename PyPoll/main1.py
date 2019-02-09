
import csv
import os

election_csv = os.path.join("election_data.csv")
   
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #creating the list
    election = list(csvreader)
#   creating removing header index            
election = election[1:]




#counting number of elements in list
count = len(election)
#print("Total Month: "+ str(len(csv_list)))


#create empty list for candidates
candidates = list()
#looping data to find candidates
for i in range(0,len(election)):
    if election[i][2] not in candidates:
        #adding to candidates if not already present in the list
        candidates.append(election[i][2])
        
#creating an empty list with len of candidates list        
votes = [0]*len(candidates)

#looping through the dataset to tally votes
for i in range(0, len(election)):

    #if the row is for 1st candidate then tally add
    if election [i][2] == candidates[0]:
        votes[0] += 1    

    #if the row is for 2nd candidate then tally add
    elif election [i][2] == candidates[1]:
        votes[1] += 1  

    #if the row is for 3rd candidate then tally add
    elif election [i][2] == candidates[2]:
        votes[2] += 1

    #if the row is for 4th candidate then tally add
    elif election [i][2] == candidates[3]:
        votes[3] += 1 

    #incase something is missing
    else:
        print("oh nooo")

#create empty list with len candidates
percentage = [0]*len(candidates)

#loop for dividing each element by total number of votes
for i in range(0,len(percentage)):

    #and try to  format it 
    percentage[i]= round(round(votes[i]/count,2)*100,3)



#print the resuts
# message1 = (f'Election Results')
# message2 = (f'------------------------------')        
# message3 = (f'Total Votes: {count}')
# message4 = (f'------------------------------')
# #looping through the 3 lists to print name of candidate||percentage||votes|| in order for each
# for i in range(0, len(candidates)):
#     print(f'{candidates[i]}: {percentage[i]}% ({votes[i]})') 
 
# message9 = (f'------------------------------')
# #find the index for max votes and get candidate name with that index value
# message10 = (f'Winner: {candidates[votes.index(max(votes))]}')
# message11 = (f'------------------------------')   

# Specify the file to write to
output_path = "C:\\Users\\Ailssa\\Documents\\Homework\\Week 3 Python Homework\\python_challenge1\\PyPoll\\Output.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:
    text_file = open("C:\\Users\\Ailssa\\Documents\\Homework\\Week 3 Python Homework\\python_challenge1\\PyPoll\\Output.txt", "w")
    


    text_file.write((f'Election Results' + "\n"))
    print(f'Election Results')
    text_file.write((f'------------------------------'+ "\n"))
    print(f'------------------------------')
    text_file.write((f'Total Votes: {count}') + "\n")
    print(f'Total Votes: {count}')
    text_file.write((f'------------------------------') + "\n")
    print(f'------------------------------')
    for i in range(0, len(candidates)):
        text_file.write(f'{candidates[i]}: {percentage[i]}% ({votes[i]})' "\n")
        print(f'{candidates[i]}: {percentage[i]}% ({votes[i]})') 

    text_file.write((f'------------------------------') + "\n")
    print(f'------------------------------')
    text_file.write((f'Winner: {candidates[votes.index(max(votes))]}') + "\n")
    print(f'Winner: {candidates[votes.index(max(votes))]}')
    text_file.write((f'------------------------------')    + "\n")
    print(f'------------------------------')
#     text_file.write(message9 + "\n")
#     text_file.write(message10 + "\n")
#     text_file.write(message11 + "\n")    


#     text_file.close()

# print(message1)
# print(message2)
# print(message3)
# print(message4)
# print(message5)
# print(message6)
# print(message7)
# print(message8)
# print(message9)
# print(message10)
# print(message11)