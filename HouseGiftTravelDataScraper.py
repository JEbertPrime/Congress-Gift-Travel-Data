import csv
import datetime
import xml.etree.ElementTree as ET
xml_file = input("what is the name of your file?\n") + '.xml'
csv_file_name = input("What is your csv file name?\n")

tree = ET.parse(xml_file)
root = tree.getroot()
print(len(root))
travel_data = []
for child in root:
        travel_row = []
        for childTwo in child:
                travel_row.append(childTwo.text)
        travel_data.append(travel_row)
# open a file for writing
travel_gifts = open(csv_file_name + '.csv', 'w', newline='')

# create the csv writer object

writer = csv.writer(travel_gifts)

writer.writerow(["Doc ID","Filer Name","Member Name","State","District","Year","Destination","Filing Type","Departure Date","Return Date","Travel Sponsor"])
writer.writerows(travel_data)


