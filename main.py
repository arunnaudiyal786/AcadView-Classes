friends = [{"Shivam":{"age":22,"rating":4.6}}]

friends

def select_friend():
  for friend in friends:
    print('age %d with rating %.2f is online' %(friend['age'], friend['rating']))

##############################
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

## Added some comment ###
def add_friend() :
    new_friend = {
        'name':"",
        'salutation':'',
        'age':0,
        'rating':0.0
    }
    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(input("Age?"))
    new_friend['rating'] = float(input("Spy rating?"))

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy_rating:
        friends.append(new_friend)
    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len(friends)


def add_friend_old():
    new_name = input("Please add your friend's name:")
    new_salutation = input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("Age?")
    new_rating = input("Spy rating?")
    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)

    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
        return len(friends_name)

def add_status(current_status_message):
    if current_status_message != None:
      print ("Your current status message is " + current_status_message + "\n")
    else:
      print ('You don\'t have any status message currently \n')

    default = input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print(str(item_position) + ". " + message)
            item_position = item_position + 1
        message_selection = int(input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    return updated_status_message

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

def start_chat(spy_name,spy_age, spy_rating):
  show_menu = True
  current_status_message=None
  while show_menu==True:
      menu_choices = ("What do you want to do? \n1. Add a status update \n2. Add a friend \n 3.Close Application \n")
      menu_choice = int(input(menu_choices))


      if menu_choice == 1:
          print ('You chose to update the status')
          current_status_message = add_status(current_status_message)

      elif menu_choice == 2:
          number_of_friend = add_friend()
          print("You have %d friends"%(number_of_friend))

      elif menu_choice == 3:
          show_menu = False



spy_name = 'Bond'
spy_salutation = 'Mr.'
spy_age = 23
spy_rating = 4.7

from spy_details import spy

question = "Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)? "
existing = input(question)

if existing=="Y":
    start_chat(spy_name, spy_age, spy_rating)
else :
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:
        print('Welcome ' + spy_name + '. Glad to have you back with us.')

        spy_salutation = input("Should I call you Mister or Miss?: ")



        spy_name = spy_salutation + " " + spy_name

        print("Alright " + spy_salutation + " " + spy_name + ". I'd like to know a little bit more about you before we proceed...")

    else:
        print("A spy needs to have a valid name. Try again please. ")

    #Lecture 2
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = int(input("What is your age? "))


    if spy_age > 12 and spy_age < 50:
        spy_rating = float(input("What is your spy rating? "))

        if spy_rating > 4.5:
            print('Great ace!')
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print('You are one of the good ones.')
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office.')
    else:
        print('Sorry you are not of the correct age to be a spy')


    print("Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard")
