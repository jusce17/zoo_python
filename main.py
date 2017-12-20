"""

@author: eden_juscelino
"""

from chart import Chart
from catalog import Catalog
from printFiles import PrintFiles
option1 = Chart()
option2 =  Catalog()
option3 = PrintFiles()
print("*" * 50)
print( "%Korea Zootopia")
print("-" * 50)

print("1. SHow Zoo Anumals Catalog")
print("2. Display Zoo Animals Charts")
print("3. Generate Zoo Animals Text Files")
action = int(input("Enter your choice: "))

#each option will fire a different method with a different action
try:
    if action == 1:
        option1.getChart()
    elif action ==2:
        option2.getImage()
    elif action ==3:
        option3.print_all_files()
    else:
        print("you've enterred the wrong info")
except IOError:
    print("there has been an error")
