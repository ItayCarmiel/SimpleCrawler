# Itay Carmiel
# 208464198
# 01
# ass 07

import re
import csv
d = {}

def get_file(name_of_file):
    l = []
    x = open(name_of_file)
    f_lines = list(x)
    #move on the file
    for line in f_lines:
        #check if the line contain "href"
        num = line.find("href")
        #if cotain
        if num != -1:
            quoted = re.compile('"[^"]*"')
            for value in quoted.findall(line):
                value = value.replace('"', '')
                l.append(value)
    #insert to the dictionry
    d[name_of_file] = l
    c = d.copy()
    #loop for the recursive call
    for i in c[name_of_file]:
       #for k in i:
        if i not in d.keys():
            get_file(i)
    x.close()

if __name__== "__main__":
  print("enter source file:")
  f = input()
  get_file(f)
  with open("result.csv", 'w', newline='') as outfile:
      csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      for k, v in d.items():
          csv_writer.writerow([k] + v)
  print("enter file name:")
  file_name=input()
  val = d[file_name]
  val.sort()
  print (val)

