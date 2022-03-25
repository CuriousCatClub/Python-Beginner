# Printing string constants
print("Hello, world!")
print("Hello, world!")
print("Captain's ship is gone!")
print('Then she said: "You need to compile the code first."')

# Printing using variables
first_name = 'Jack'
last_name = 'Sparrow'
rank = 'Captain'
number_of_hats = 1

# Below line is going to create an error - uncomment and run to chech this
#print(rank + ' ' + first_name + ' ' + last_name + ' has only ' + number_of_hats +' hat.')

# The below options will work :)
print(rank + ' ' + first_name + ' ' + last_name + ' has only ' + str(number_of_hats) +' hat.')
print("Our hero {} {} {} has only {} hat.".format(rank, first_name, last_name, number_of_hats))
print("Our hero {3} {2} {1} has only {0} hat.".format(rank, first_name, last_name, number_of_hats))

# Even more printing
pi = 3.14159
print("Number PI: {0:.2f}".format(pi))
print("Number PI: {0:15.2f}".format(pi))
print("Number PI: {0:10.4f}".format(pi))

print()
print("END OF THE LESSON".center(40, '-'))

