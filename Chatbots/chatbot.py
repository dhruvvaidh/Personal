class contact_details:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email_id = ""
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

    def enter_data(self, a):
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.email_id = input("Email ID: ")
        self.phone_number = input("Phone Number: ")
        self.state = input("State: ")
        self.city = input("City: ")
        self.board = input("Board: ")
        self.check_board()
        self.grade = input("Grade: ")
        if int(a) == 2:
            self.account_type = 'trial'
        elif int(a) == 3:
            self.account_type = 'member'


print("Press 1 to know about the Courses being offered")
print("Press 2 to Book a Free Trial")
print("Press 3 for Creating a New Account")
print("Press 4 for Customer Care Details ")
print(" Type 'bye' to exit this conversation")
choice = input()
if int(choice) == 1:
    print("Courses")
elif int(choice) == 2:
    print("Contact Details for Booking a Free Trial")
    user = contact_details()
    user.enter_data(choice)

elif int(choice) == 3:
    print("Contact Details for Creating a New Account")
    user = contact_details()
    user.enter_data(choice)
elif int(choice) == 4:
    print("Customer Care")
else:
    print("Invalid input")
