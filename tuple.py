#creating the tuple
fruits=("apple","banana","mango","orange")
print(f"Created tuple:{fruits}")

#Accessing the elements from tuple
print(f"first element :{fruits[0]}")
print(f"last element :{fruits[-1]}")
print(f" 1 to 3 element :{fruits[1:3]}")

#Nested tuple
mixed_tuple= ("phones",123,("Redmi,Oneplus,iphone"))
print(f"Nested tuple:{mixed_tuple}")

#Accessing the tuple 
print(f"Nested tuple elements:{mixed_tuple[2]}")

#Accessing  the element form nested tuple
print(f"Nested tuple element:{mixed_tuple[2][5]}")

#Repeatation of tuple
fruits=("apple","banana","mango","orange")
repeated_tuple = fruits *3
print(f"Nested tuple:{repeated_tuple}")

#Concatenation of tuple
more_fruits = ("dragon fruit","pineapple")
combined_fruits = fruits + more_fruits
print(f"concatenation of tuple:{combined_fruits}")