#create the dictionary 
car = {'BMW':{'color':'White','year':'2020'},
       'Mercedes benz':{'color':'Red','year':'2022'},
       'Toyota':{'color':'Silver','year':'2024'}
       }
print(f"created dictionary:",car)

#Accessing the elements
BMW_details = car['BMW']
print(f"\n deatils of BMW ",BMW_details)

#updating the dictionary 
car['BMW'] = {'color':'golden','year':'2018'}
print(f"\n updated deatils of BMW ", car['BMW'])

#removing the elements from dictonary 
del car['Mercedes benz']
print(f"Dictionary after removing the mercedes benz",car)
      
#merging the dictonary 
new_car_add ={'BMW M3':{'color':'White','year':'2020'},
       'mercedes c class':{'color':'Red','year':'2022'}}
car.update(new_car_add)
print(f"dictonary after merging ",car)