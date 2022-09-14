# Program1
# Bhargav Reddy Lankireddy
# Id: 00798146
# Week 3 Program #3 List and List Manuplations


# Create a List Of Cities
cityList = ["Hartford","NewHaven","Stamford","Bridgeport","Waterbury"]

# Create a ZIPLIST for cities
zipList = ['06103','06511','06901','06601','06701']


# Composite List Creation
compList=[]

dup = cityList
for i in range(len(cityList)):
	compList.append(cityList[i]+ ":" +zipList[i])

# Index on Individual List
cityIndex = cityList.index("NewHaven")

print(f"Index on cityList - NewHaven {cityIndex}")

zipIndex = zipList.index('06511')

print(f"Index on zipList - 06511 {zipIndex}")

#Index on Composite List

compIndex = compList[1]

print(f"Cpmposite index is {compIndex}")


# Append on Individual List


#Appending a new city to cityList

cityList.append("Milford")

#Appending a new zipCode to zipList

zipList.append('06460')


# Append on Composite List
cityLen = len(cityList)
zipLen = len(zipList)

compList.append(cityList[cityLen-1]+ ":" +zipList[zipLen-1])

print(compList)


# Size of Individual List

sizeCityList = len(cityList)
print(f"Size of the cityList {sizeCityList}")

sizeZip = len(zipList)
print(f" Size of the zipList {sizeZip}")

# Size of Composite List

sizeComposite = len(compList)
print(f" Size of composite size {sizeComposite}")


# Indexing from End to Beginning

cityIndexing = cityList[::-1]
print(f"city Indexing {cityIndexing}")


# zipList Indexing

zipListIndexing = zipList[::-1]
print(f"city Indexing {zipListIndexing}")

#Composite List Indexing

compListIndexing = compList[::-1]
print(f"city Indexing {compListIndexing}")




# Slicing the List from 3rd to Last
citySlicing = cityList[3:]
print(f"city Slicing {citySlicing}")

# Zipcode slicing
zipslicing = zipList[3:]
print(f"city Slicing {zipslicing}")



# Formatted Output

print(f"Cities : {cityList}")
print(f"Zip codes : {zipList}")

for i in range(len(cityList)):
	print(f'City #{i} : {cityList[i]} . Zip #{i} : {zipList[i]}')

























	


	
