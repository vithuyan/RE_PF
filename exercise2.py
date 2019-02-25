#Exercise 2
# Pick three names and store them in a list.
#
# Prompt the user to enter their name. If their name is one of the names in the list, display a greeting message that includes their name.
# If their name isn't in the list, display "Who goes there?"
three_names = ['Billy', 'John', 'Sam']
print("What's your name?")
user_name = input()
if user_name in three_names:
    print('Hello.')
else:
    print("Who goes there?")
