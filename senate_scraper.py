
# coding: utf-8

# In[1]:


import csv
import datetime
import xml.etree.ElementTree as ET


# In[38]:


xml_file = input("what is the name of your file (without xml extension)?\n") + '.xml'
csv_file_name = input("What is your csv file name (without csv extension)?\n")
#See the house scraper for most of the stuff I didn't comment out here
tree = ET.parse(xml_file)
root = tree.getroot()
#For debugging, and knowing exactly how many entries there are
print(root)
print(len(root))




# In[34]:


travel_data = []
#Every nested for loop here goes one level further into the xml tags (or whatever they're called, IDK)
#All you really need to know about this block is that working with xml files sucks and I hate it
#All the loops with "values" are for getting the info from the attributes in a level, and the other loops go one level deeper
for name_child in root:
    for office_child in name_child:
        for report_child in office_child:
            d = {}
            for value in name_child.attrib.items():
                d[value[0]] = value[1]
            for value in office_child.attrib.items():
                d[value[0]] = value[1]
            for value in report_child.attrib.items():
                d[value[0]] = value[1]
            for report_title_child in report_child:
                for value in report_title_child.attrib.items():
                    d[value[0]] = value[1]
            print(d)
            travel_data.append(d)

            
  


# In[56]:


travel_gifts = open(csv_file_name + '.csv', 'w', newline='')

# create the csv writer object

writer = csv.writer(travel_gifts)
#Because this stores multiple entries for the same employee on the same row, I just made the header row extend all the way out for all of them
#Sorry for how poor of a workaround this is
print(travel_data[0].keys())
writer.writerow(list(travel_data[0].keys()))
for item in travel_data:
    write_list = []
    for key, val in item.items():
        write_list.append(val)
    print(write_list)
    writer.writerow(write_list)
# writer.writerows(travel_data)



# why is this just writing the header row over and over????????


# In[55]:


for item in travel_data:
    for key, val in item.items():
#         print(key)
        print(val)
        print()

