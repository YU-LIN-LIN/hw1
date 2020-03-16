# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061237.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:
      data.append(row)    # put row into data
   
#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

target_data = list(filter(lambda item: (item['station_id'] == 'C0A880' or item['station_id'] == 'C0F9A0' or item['station_id'] == 'C0G640' or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260'), data))

# Retrive ten data points from the beginning.

# target_data = data[:10]


#=======================================


# Part. 4

#=======================================

# Print result

n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
SP_A880 = 0.0
n_A880 = 0.0
SP_F9A0 = 0.0
n_F9A0 = 0.0
SP_G640 = 0.0
n_G640 = 0.0
SP_R190 = 0.0
n_R190 = 0.0
SP_X260 = 0.0
n_X260 = 0.0

for i in range(len(target_data)):
   if (target_data[i]['station_id'] == 'C0A880') :
      if (target_data[i]['PRES'] == '-99.000' or target_data[i]['PRES'] == '-999.000') :
         n0 = 1
         target_data[i].popitem(target_data[i]['PRES'])
      else :
         SP_A880 = SP_A880 + float(target_data[i]['PRES'])
         n_A880 = n_A880 + 1
   elif (target_data[i]['station_id'] == 'C0F9A0') :
      if (target_data[i]['PRES'] == '-99.000' or target_data[i]['PRES'] == '-999.000') :
         n1 = 1
         target_data[i].popitem(target_data[i]['PRES'])
      else :
         SP_F9A0 = SP_F9A0 + float(target_data[i]['PRES'])
         n_F9A0 = n_F9A0 + 1
   elif (target_data[i]['station_id'] == 'C0G640') :
      if (target_data[i]['PRES'] == '-99.000' or target_data[i]['PRES'] == '-999.000') :
         n2 = 1
         target_data[i].popitem(target_data[i]['PRES'])
      else :
         SP_G640 = SP_G640 + float(target_data[i]['PRES'])
         n_G640 = n_G640 + 1
   elif (target_data[i]['station_id'] == 'C0R190') :
      if (target_data[i]['PRES'] == '-99.000' or target_data[i]['PRES'] == '-999.000') :
         n3 = 1
         target_data[i].popitem(target_data[i]['PRES'])
      else :
         SP_R190 = SP_R190 + float(target_data[i]['PRES'])
         n_R190 = n_R190 + 1
   elif (target_data[i]['station_id'] == 'C0X260') :
      if (target_data[i]['PRES'] == '-99.000' or target_data[i]['PRES'] == '-999.000') :
         n4 = 1
         target_data[i].popitem(target_data[i]['PRES'])
      else :
         SP_X260 = SP_X260 + float(target_data[i]['PRES'])
         n_X260 = n_X260 + 1

if (n0 == 1) :
   avg_A880 = str(None)
else :
   avg_A880 = SP_A880 / n_A880
   avg_A880 = str(format(avg_A880, '.2f'))
if (n1 == 1) :
   avg_F9A0 = str(None)
else :
   avg_F9A0 = SP_F9A0 / n_F9A0
   avg_F9A0 = str(format(avg_F9A0, '.2f'))
if (n2 == 1) :
   avg_G640 = str(None)
else :
   avg_G640 = SP_G640 / n_G640
   avg_G640 = str(format(avg_G640, '.2f'))
if (n3 == 1) :
   avg_R190 = str(None)
else :
   avg_R190 = SP_R190 / n_R190
   avg_R190 = str(format(avg_R190, '.2f'))
if (n4 == 1) :
   avg_X260 = str(None)
else :
   avg_X260 = SP_X260 / n_X260
   avg_X260 = str(format(avg_X260, '.2f'))


print('''[['C0A880',''', avg_A880 + '],', '''['C0F9A0',''', avg_F9A0 + '],', '''['C0G640',''', avg_G640 + '],', '''['C0R190',''', avg_R190 + '],', '''['C0X260',''', avg_X260 + ']]')   

#print("['C0R190', ", target_data[2]['PRES'], "]")

#========================================