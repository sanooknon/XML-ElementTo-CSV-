import io
import sys
import csv
import os
import xml.etree.ElementTree as ET
# load and parse the file
path = input('XML Path:')

for filename in os.listdir(str(path)):
    print(filename)
    xmlTree = ET.parse(str(path)+'\\'+str(filename))
    elemList = []
    for elem in xmlTree.iter():
        elemList.append(elem.tag)
    # now I remove duplicities - by convertion to set and back to list
    elemList = list(set(elemList))
    # Just printing out the result
    print(elemList)
    with open(str(path)+'\\'+str(filename)+'.csv' , 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\n')
        writer.writerow(elemList)