
############################### Spy Chat Application ##########################################################
from spy_details import spy, Spy, ChatMessage
import csv
from steganography.steganography import Steganography

friends = []

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']



def select_a_friend():
    item_number = 0

    for friend in friends:

        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1

    friend_choice = int(input("Choose from your friends"))
    friend_choice_position = friend_choice - 1

    return friend_choice_position


def send_message():

  friend_choice = select_a_friend()

  original_image = raw_input("What is the name of the image?")
  output_path = 'output12.jpg'
  text = raw_input("What do you want to say?")

  Steganography.encode(original_image, output_path, text)
  new_chat = ChatMessage(message=text, sent_by_me=True)


  friends[friend_choice].chats.append(new_chat)

  print "Your secret message is ready!"

  with open("chats.csv", 'a') as chats_data:
      write = csv.writer(chats_data)
      write.writerow([friends[friend_choice].name, text, new_chat.time, new_chat.sent_by_me])

  print "Your secret message image is ready!"




def read_message():

  sender = select_a_friend()

  output_path = raw_input("What is the name of the file?")

  secret_text = Steganography.decode(output_path)

  print(secret_text)

  new_chat = ChatMessage(message=secret_text, sent_by_me=False)
  friends[sender].chats.append(new_chat)

  print "Your secret message has been saved!"

  with open("chats.csv", 'ab') as chats_data:
      write = csv.writer(chats_data)
      write.writerow([friends[sender].name, secret_text, new_chat.time, new_chat.sent_by_me])

  print "Your secret message has been saved!"




def add_friend():

    name = raw_input("Please add your friend's name: ")
    salutation = raw_input("Are they Mr. or Ms.?: ")
    name = salutation + " " + name

    age = int(raw_input("Age?"))
    rating = float(raw_input("Spy rating?"))

    if len(name) > 0 and age > 12 and rating >= spy.rating:

        new_friend = Spy(name=name, salutation=salutation, age=age, rating=rating)

        friends.append(new_friend)

        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.rating, new_friend.age, new_friend.is_online])

        print 'Friend Added!'

    else:

        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')

    return len(friends)


def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:

        print ("Your current status message is " + current_status_message + "\n")

    else:

        print ('You don\'t have any status message currently \n')

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = str(raw_input("What status message do you want to set?"))

        if len(new_status_message) > 0:

            #STATUS_MESSAGES.append(new_status_message)

            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:

            print(str(item_position) + ". " + str(message))
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:

            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    return updated_status_message




def load_friends():
    with open('friends.csv', 'r') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy = Spy(name=row[0], salutation=row[1], age=int(row[3]), rating=float(row[2]))
            friends.append(spy)






#def start_chat(spy_name, spy_age, spy_rating):
def start_chat(spy):

    show_menu = True
    current_status_message = None

    spy.name=spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard"

        load_friends()



    while show_menu == True:

        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read the contents of friends list \n " \
                       "6. Close Application \n"
        menu_choice = int(input(menu_choices))

        if menu_choice == 1:
            print('You chose to update the status')
            current_status_message = add_status(current_status_message)

        elif menu_choice == 2:
            number_of_friend = add_friend()
            print("You have %d friends\n" % (number_of_friend))


        elif menu_choice == 3:

            send_message()

        elif menu_choice == 4:

            read_message()

        elif menu_choice == 5:

            for data in friends:
                print("Name is "+str(data.name)+ " age is "+str(data.age)+ " rating is "+ str(data.rating))

            #read_old_chat()
            pass

        else:

            show_menu = False




question = "Continue as " + spy.salutation + " " + spy.name + "(Y/N)? "
existing = raw_input(question)

if existing == 'Y':

    start_chat(spy)
else:
    spy.name = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = input("Should I call you Mr. or Ms.?: ")

        spy.age = input("What is your age?")

        spy.rating = input("What is your spy rating?")

        spy.is_online = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'


