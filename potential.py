#potential question one

# def linear_search(list_l, key):
#     """
#     return true if key is in the list_l, false otherwise

#     All the elements in list_l are distinct
#     """


# answer version 1- 
# for i in list_l:
#         if i == key:
#             return True
#     return False

# # answer version 2- 
# def linear_search(list_l, key):
#     """
#     return true if key is in the list_l, false otherwise

#     All the elements in list_l are distinct
#     """
#     flag = False
#     for i in list_l:
#         if i == key:
#             flag = True
#             break
#     return flag


#complexity of a linear search function
#we use O(n)
#O(1) meanas it is teh first element in the list and O(n) is the last element


# define a function, the function will take an parameter list and take a key
# check if the element is in the list and return the index of the element
# if the element does not exist in the list then return None or false (obviously you can never return an index)


#find an element in a list via a linear search - O(n)
#Insert/Append an element in the end of the list - O(1)
#Insert an element in the beginning of the list - O(n)


#deifne a function that takes one parameter n (n>0) and reads n integers from the user
#if the integer is positive then add it to the list
# function will return the list

# def read_int(n):
#     pos_int = []
#     for i in range(n):
#         try:
#             num = int(input(f"Enter an integer {i+1}/{n}: "))
#             if num > 0:
#                 pos_int.append(num)
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")
#     return pos_int

# n = int(input("Enter the number of integers you need: "))
# pos_int = read_int(n)
# print("The list of positive integers is:", pos_int)





