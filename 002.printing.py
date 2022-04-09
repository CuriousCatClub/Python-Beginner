# Printing string constants
print("Hello, world!")
print('Hello, world!')
print("Captain's ship is gone!")
print('She said: "In C you need to compile the source code first."')

# Printing using variables
first_name = 'Jack'
last_name = 'Sparrow'
rank = 'Captain'
number_of_hats = 1

# Below line is going to create an error - uncomment and run to check it
#print(rank + ' ' + first_name + ' ' + last_name + ' has only ' + number_of_hats +' hat.')

# The below options will work :)
print(rank + ' ' + first_name + ' ' + last_name + ' has only ' + str(number_of_hats) +' hat.')
print("Our hero {} {} {} has only {} hat.".format(rank, first_name, last_name, number_of_hats))
print("Our hero {3} {2} {1} has only {0} hat.".format(rank, first_name, last_name, number_of_hats))
print(f"Our hero {rank} {first_name} {last_name} has only {number_of_hats} hat.")

# Even more printing
pi = 3.14159
print("Number PI: {0:.2f}".format(pi))
print("Number PI: {0:15.2f}".format(pi))
print("Number PI: {0:10.4f}".format(pi))

# Or the same with newest format
print(f"PI = {pi:.2f}")
print(f"PI: {pi:15.2f}".format(pi))
print(f"PI: {pi:10.4f}".format(pi))

print()
print("END OF THE LESSON".center(40, '-'))
