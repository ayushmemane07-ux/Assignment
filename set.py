#creating the set 
my_set_1={5,10,13,14}
my_set_2={6,11,14,18}
print(f"Set 1:{my_set_1}")
print(f"Set 2:{my_set_2}")

#Accessing the elements using for loop
for element in my_set_1:
    print(f" Is 11 in set 1:{11 in my_set_1}")

#Union of set 
union_set = my_set_1.union(my_set_2)
print(f"Union of set 1 and 2:{union_set}")

#Intersection of set
intersection_set = my_set_1.intersection(my_set_2)
print(f"intersection of set 1 and 2:{intersection_set}")

#Differnce of set 
difference_set_1_2 = my_set_1.difference(my_set_2)
difference_set_2_1 = my_set_2.difference(my_set_1)
print(f"Difference (set 1- set 2):{difference_set_1_2 }")
print(f"Difference (set 2- set 1):{difference_set_2_1 }")