import csv
import datetime
import xml.etree.ElementTree as ET
xml_file = input("what is the name of your file?\n") + '.xml'
csv_file_name = input("What is your csv file name?\n")
#See the house scraper for most of the stuff I didn't comment out here
tree = ET.parse(xml_file)
root = tree.getroot()
#For debugging, and knowing exactly how many entries there are
print(root)
print(len(root))
travel_data = []
#Every nested for loop here goes one level further into the xml tags (or whatever they're called, IDK)
#All you really need to know about this block is that working with xml files sucks and I hate it
#All the loops with "values" are for getting the info from the attributes in a level, and the other loops go one level deeper
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
#Because this stores multiple entries for the same employee on the same row, I just made the header row extend all the way out for all of them
#Sorry for how poor of a workaround this is
writer.writerow(["Filer First Name","Filer Last Name","Office Name","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title","Year","Begin Travel Date","End Travel Date","Date Received","Transaction Date","Document Pages","Reports Title"])
writer.writerows(travel_data)

