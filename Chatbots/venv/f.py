flag = True
print("My name is Jarvis."+"\n"+"Let's have a conversation."+"\n"+"If you want to exit, just type 'Bye'.")
contacts = open("/content/sample_data/contacts.txt", 'x')
contacts = open("/content/sample_data/contacts.txt", 'r+')
while (flag==True):
  class contact_details:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email_id =""
        self.phone_number = ""
        self.state = ""
        self.city = ""
        self.board = ""
        self.grade = ""
        self.account_type = ""
    def check_board(self):
        Flag = 0
        while Flag != 1:
            if self.board.lower() != "cbse" or self.board.lower() != "isc" or self.board.lower() != "state":
                print("Invalid input....")
                print("Please Write again")
                self.board = input("Board: ")
            else:
                Flag = 1
    def enter_data(self,a):
      self.first_name = input("First Name: ")
      self.last_name = input("Last Name: ")
      self.email_id = input("Email ID: ")
      self.phone_number = input("Phone Number: ")
      self.state = input("State: ")
      self.city = input("City: ")
      self.board = input("Board: ")
      check_board()
      self.grade = input("Grade: ")
      if (int(a)==2):
        self.account_type = 'trial'
      elif (int(a)==3):
        self.account_type = 'member'



  user_response = user_response.lower()
  user_response = input()
  if (user_response != 'bye'):
    if (user_response =='thanks' or user_response =='thank you'):
      flag = False
      print("BOT: You are welcome.......")
    else:
      if (greet(user_response) != None):
        print("BOT: "+greet(user_response))
        print("BOT: ",end="")
        print("Press 1 to know about the Courses being offered")
        print("Press 2 to Book a Free Trial")
        print("Press 3 for Creating a New Account")
        print("Press 4 for Customer Care Details ")
        print(" Type 'bye' to exit this conversation")
        if int(user_response) == 1:
          print("Courses")
        elif int(user_response) == 2:
          print("Enter Contact Details for Booking a Free Trial")
          user = contact_details()
          user.enter_data(user_response)
          f.write(user)

        elif int(user_response) == 3:
          print("Enter Contact Details for Creating a New Account")
          user = contact_details()
          user.enter_data(user_response)
          f.write(user)

        elif int(user_response) == 4:
          print("Customer Care Contact Details")
        else:
          print("Invalid input, please try again....")

          flag = False
  """
      else:
        sent_tokens.append(user_response)
        word_tokens = word_tokens + nltk.word_tokenize(user_response)
        final_words = list(set(word_tokens))
        print("BOT: ",end="")
        print(response(user_response))
        sent_tokens.remove(user_response)
  """
  else:
  flag = False
    print("BOT: Goodbye!!......")