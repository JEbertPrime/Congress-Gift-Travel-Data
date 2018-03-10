import csv
import datetime
import xml.etree.ElementTree as ET
#Retrieves user input for name of local file
xml_file = input("what is the name of your file?\n") + '.xml'
csv_file_name = input("What is your csv file name?\n")
#I just started using ElementTree, so I'm not 100% on this stuff
tree = ET.parse(xml_file)
root = tree.getroot()
#This is for showing how many entires there are.
print(len(root))
travel_data = []
#For the House data, all the entires are stored as text. This iterated through all the entries, and stores all fields for an entry as cells
#in a row.
for child in root:
        travel_row = []
        for childTwo in child:
                travel_row.append(childTwo.text)
        travel_data.append(travel_row)
# open a file for writing
travel_gifts = open(csv_file_name + '.csv', 'w', newline='')

# create the csv writer object

writer = csv.writer(travel_gifts)
#headers
writer.writerow(["Doc ID","Filer Name","Member Name","State","District","Year","Destination","Filing Type","Departure Date","Return Date","Travel Sponsor"])
writer.writerows(travel_data)


