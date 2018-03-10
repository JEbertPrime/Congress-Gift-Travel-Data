import csv
import datetime
import xml.etree.ElementTree as ET
xml_file = input("what is the name of your file?\n") + '.xml'
csv_file_name = input("What is your csv file name?\n")

tree = ET.parse(xml_file)
root = tree.getroot()
print(root)
print(len(root))
travel_data = []
for child in root:
        travel_row = []
        for values in child.attrib.items():
                travel_row.append(values[1])
        for childTwo in child:
                for values in childTwo.attrib.items():
                        travel_row.append(values[1])                
                for childThree in childTwo:
                        for values in childThree.attrib.items():
                                travel_row.append(values[1])
                        for childFour in childThree:
                                for values in childFour.attrib.items():
                                        travel_row.append(values[1])
        travel_data.append(travel_row)
# open a file for writing
travel_gifts = open(csv_file_name + '.csv', 'w', newline='')

# create the csv writer object

writer = csv.writer(travel_gifts)

writer.writerow(["Filer First Name","Filer Last Name","Office Name","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title"])
writer.writerows(travel_data)

