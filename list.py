
#Creating the list 
fruits=["apple","mango","banana","dragon fruit"]
print(f"Original list :{fruits}")

#Accessing the elements from list 
print(f"first element :{fruits[0]}")
print(f"last element :{fruits[-1]}")
print(f" 1 to 3 element :{fruits[1:3]}")

#Insering the new element in the list 
fruits.insert(2,"pineapple")
print(f"After inserting element list :{fruits}")

#Adding the element at last
fruits.append("orange")
print(f"After adding element list :{fruits}")

#Removing the elements 
fruits.remove("pineapple")
print(f"After removing element list :{fruits}")

#sorting the elements
fruits.sort()
print(f"After sorting element list :{fruits}")

#reverse list element 
fruits.sort(reverse=True)
print(f"After reverse list element:{fruits}")