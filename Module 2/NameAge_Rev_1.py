#
#  Patrick D. Pattison
#  IT-140-J5082 2-3 Assignment: PyCharm Introduction Part A
#  Southern Hew Hampshire University
#
#  08 May 2021 - Initial Coding...
#  09 May 2021 - Removed datetime package depedancy and hard coded the 
#                current year in case using external packages are not allowed.
#

#  Requirements:  Prompt user for their name(string) and age(int).
#                 The age should be used to calculate the year of birth of the user.
#  Output:  "Hello <name>!  You were born in <year>."
#


#  First off, let's set the current year...
current_year = 2021

#  Secondly, let's prompt the user for the information we need...
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

#  Thirdly, let's calculate the users year of birth.
#  This is a very crude implementation as it doesn't take into account
#   when in the year they were born.  There could be an off by one error
#   if the users birthday for this year hasn't occurred yet.
birth_year = current_year - user_age

#  Finally, let's print out the output.
print("\nHello {}!  You were born in {}.\n".format(user_name, birth_year))
