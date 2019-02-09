# -*- coding: utf-8 -*-


import csv
import os

# create path
financial_csv = os.path.join("budget_data.csv")
   
#open and read the file   
with open(financial_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #creating the list
    csv_list = list(csvreader)
#    csv_header = next(csvfile)
#    
#    print(f"Header: {csv_header}")
#    for row in csvreader:
#        if float(row[1]) >= 5:
#            print(row)
##            
#        
#    sum = 0
#    for row in csvreader:
#        sum += row
#        print (sum)
#    return sum
#    #print (sum)    

#creating removing header index            
csv_list = csv_list[1:]

#counting number of elements in list
count = len(csv_list)



# creating blank int variable
net_profit = 0
average = 0
maxchange = 0
maxchangemonth = 0 
minchange = 10000000000000000000000
minchangemonth = 0
#starting loop around cvs_list index
for i in range(0, len(csv_list)):
    #adding to the existing net_profit added to the element value
    net_profit += int(csv_list[i][1])
    
    #looping all but the difference of last element 
    if i < len(csv_list)-1:
        average += int(csv_list[i+1][1])-int(csv_list[i][1])
        
        # calculate greatest increase in profits
        if maxchange < (int(csv_list[i+1][1])-int(csv_list[i][1])):
            maxchange = (int(csv_list[i+1][1])-int(csv_list[i][1]))
            maxchangemonth = csv_list[i+1][0]
        
        # calculate greatest decrease in profits
        if minchange > (int(csv_list[i+1][1])-int(csv_list[i][1])):
            minchange = (int(csv_list[i+1][1])-int(csv_list[i][1]))
            minchangemonth = csv_list[i+1][0]
avg = round(average/(count-1),2)        

message1 = (f'Financial Analysis')
message2 = (f'------------------------------')        
message3 = (f'Total Month: {count}')
message4 = (f'Total: ${net_profit}')
message5 = (f'Average Change: ${avg}')
message6 = (f'Greatest Increase in Profits: {maxchangemonth} (${maxchange})')
message7 = (f'Greatest Decrease in Profits: {minchangemonth} (${minchange})')
    
# Specify the file to write to
output_path = "C:\\Users\\Ailssa\\Documents\\Homework\\Week 3 Python Homework\\python_challenge1\\PyBank\\Output.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:
    text_file = open("C:\\Users\\Ailssa\\Documents\\Homework\\Week 3 Python Homework\\python_challenge1\\PyBank\\Output.txt", "w")

    text_file.write(message1 + "\n")
    text_file.write(message2 + "\n")
    text_file.write(message3 + "\n")
    text_file.write(message4 + "\n")
    text_file.write(message5 + "\n")
    text_file.write(message6 + "\n")
    text_file.write(message7 + "\n")

    text_file.close()

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)



  