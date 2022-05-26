# Pyhton to-do app Project
user_input = 'random'
# create a list for storing items
data = list()
# I am going to create 4 options
# 1. Add an item
# 2. Mark as Done
# 3. View Items
# 4. Exit

# and create menu items using function


def showMenu():
	print("Menu:")
	print("1. Add an item:")
	print("2. Mark as Done:")
	print("3. View Items:")
	print("4. Exit:")


while user_input != '4':

	showMenu()
	user_input = input("Enter Your Choice: ")

	if user_input == '1':
		item = input("What is to be done ? ")
		data.append(item)
		print("Added item:", item)
	elif user_input == '2':
		item = input("What is to be marked as Done ")

		# if item is present in data list then remove it from list
		# else print item does not exist in the list

		if item in data:
			data.remove(item)
			print("Removed item:", item)
		
# I dont know were is the problem I think with the space or indentation !!
		elif  user_input == '3':

			print("List of TO-DO Items: ")
			for items in data:
				print(items)
	    
		elif user_input == '4':
	    	print("Good Luck & Good Bye :)") 

	else:
		    print("Item does not exist in the to-do list ")   	

 