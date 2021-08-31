#!/usr/bin/env python
# coding: utf-8

# Importing the Libraries

# In[1]:


import random
import re
import string
from os import system, name

import nltk


# import pickle


# In[2]:


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Importing the corpus

# In[3]:


f = open("chatbot.txt", 'r', errors='ignore')
raw_doc = f.read()

# Pre Processing and Text Case Handling

raw_doc = raw_doc.lower()  # converts everything inside the file into lower case
nltk.download('punkt')  # we are going to use punkt tokenizer as it is pre trained for making chatbots.
nltk.download('wordnet')  # we are going to use the wordnet dictionary
sent_tokens = nltk.sent_tokenize(
    raw_doc)  # converts doc into a list of sentences(each element in this list is a sentance)
word_tokens = nltk.word_tokenize(raw_doc)  # converts doc into a list of words(each element in this list is a word)

# Example of Sentence Token

# In[4]:


# sent_tokens[:2]


# Example of Word Token

# In[5]:


# word_tokens[:2]


# Text Pre-Processing

# In[6]:


# WordNet dictionary i already included in the nltk library
lemmer = nltk.stem.WordNetLemmatizer()


# WordNet is a semantically-oriented dictionary of English in NLTK
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


# We are removing the punctuations from the text here
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Greeting Function

# In[7]:


# this list contains all the possible greetings a user can make to the bot
GREET_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey"]
# this list contains some responses the bot can make after the user's greetings 
GREET_OUTPUTS = ["hi", "hey", "*nods*", "hi there", "hello", "I'm glad! that you're talking to me"]
pattern = re.compile('|'.join(GREET_INPUTS))


def greet(sentence):
    flag = 0
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            flag = 1
        elif len(re.findall(pattern, word.lower())) > 0:
            flag = 1
    # When the user enters a sentence, it is being split into words and each is being checked inside the GREET_INPUTS
    # list
    if (flag == 1):
        return random.choice(GREET_OUTPUTS)


# Response Generation

# In[8]:


# We use Text Frequency and Inverse Document Frequency Vectorizer is used to find how many times a term is present in
# the corpus(Text Frequency) Inverse Document Frequency is used to find out how rare a term is in the corpus and it
# is converted into a vector form which is machine readable

from sklearn.feature_extraction.text import TfidfVectorizer

# After we obtain the the Bag of Words and their correcponding vectors, we use the cosine functionality to give a
# normalized output

from sklearn.metrics.pairwise import cosine_similarity


# In[9]:


# We are converting the bag of words into vector form so that it is machine readable
# These vectors are converted into matrices which will be used to generate responses
def response(user_response):
    robo1_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo1_response = "I'm Sorry" + "/n" + "I don't understand you"
    else:
        robo1_response = robo1_response + sent_tokens[idx]
        return robo1_response


# Main Menu

# In[10]:


def main_menu():
    print("For example, reply with '1' for Eduauraa Information \n ")
    print("1.Eduauraa Information")
    print("2.Learn with Eduauraa bot")
    print("3.Subscription Plans")
    print("4.Refer & Earn")
    print("5.Social media connect")
    print("6.Request a live session/demo")
    print("7.Customer Support")
    print("\n Type 'bye' to exit this conversation")
    print("\n \n Download the Eduauraa App Now - ")
    print("Link: ")


# Keywords

# In[11]:


input0 = ['0', 'back', 'home', 'main', 'refresh', 'main list', 'menu', 'refersh', 'restart']
input1 = ['1', 'eduauraa information', 'info', 'information', 'about eduauraa', 'about', 'boards', 'board', 'grade',
          'class', 'language', 'english', 'hindi', 'marathi']
input2 = ['2', 'learn', 'start learning', 'bot', 'explain', 'physics', 'chemistry', 'maths', 'biology']
input3 = ['3', 'plans', 'subscribe', 'subscription', 'money', 'pricing']
input4 = ['4', 'refer & earn', 'referral program', 'gifts', 'rewards', 'vouchers']
input5 = ['5', 'social media', 'facebook', 'twitter', 'instagram', 'linkedin', 'telegram']
input6 = ['6', 'live session', 'trial', 'book demo', 'demo', 'trial', 'try']
input7 = ['7', 'customersupport', 'support', 'issue', 'ticket', 'error', 'help']
input8 = ['8', 'physics', 'phy']
input9 = ['9', 'chemistry', 'chem']
input10 = ['10', 'biology', 'bio']
input11 = ['11', 'mathematics', 'mat', 'maths']
inputx = ['exit', 'close', 'bye', 'dnd', 'quit', 'stop']


def trigger(sentence, inputs):
    pattern = re.compile('|'.join(inputs))
    flag = 0
    for word in sentence.split():
        if word.lower() in inputs:
            flag = 1
        elif len(re.findall(pattern, word.lower())) > 0:
            flag = 1
    # When the user enters a sentence, it is being split into words and each is being checked inside the GREET_INPUTS
    # list
    if (flag == 1):
        return True
    else:
        return False


# Conversation

# In[14]:


flag = True
print("BOT: ", end="")
print("Hi, \n Welcome to Eduauraa \n We are thrilled to have you aboard \n Lets start your learning experience -")
print("If you want to exit, just type 'Bye'.")
# with open('contact', 'wb') as contacts_file
while (flag == True):
    """
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
        def enter_data(self,a):
            self.first_name = input("First Name: ") 
            self.last_name = input("Last Name: ") 
            self.email_id = input("Email ID: ") 
            self.phone_number = input("Phone Number: ")
            self.state = input("State: ") 
            self.city = input("City: ") 
            self.board = input("Board: ")
            self.grade = input("Grade: ") 
            if (int(a)==2):
                self.account_type = 'trial'
            elif (int(a)==3):
                self.account_type = 'member'
        """

    user_response = input()
    user_response = user_response.lower()
    if trigger(user_response, inputx) == False:
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("BOT: You are welcome.......")
        else:
            if greet(user_response) != None:
                print("BOT: " + greet(user_response))
                print("BOT: ", end="\n")
                main_menu()
            if not trigger(user_response, input0):
                if trigger(user_response, input1):
                    states = ["Maharashtra", "Rajasthan", "Bihar", "Chhattisgarh", "Tamil Nadu", "Uttar Pradesh",
                              "Madhya Pradesh"]
                    print("BOT: ", end="")
                    print(
                        "Eduauraa is a premium digital learning website for all your educational needs! \n We provide "
                        "educational content according to the syllabi of: \n")
                    print("\t1. ICSE \n\t2. CBSE and \n\t3. 7 State Boards:")
                    for i in states:
                        print("\n\t\t" + i)
                    print(
                        "We cover the subjects of Mathematics and Science for classes 6-10 and Mathematics, Physics, "
                        "Chemistry and Biology for classes 11-12")
                    print(
                        "\n Our videos are available in Hindi and English so that you can learn in the best way "
                        "possible!")
                    print("\n We also have a bunch of features like: ")
                    print(
                        "\n\t60000+ videos \n\t5000+ E-books \n\t50000+ test papers \n\t2500+ Mind Maps \n\tEduauraa "
                        "Proficiency Quotient")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response, input2):
                    print("BOT: ", end="")
                    print("Learn with Eduauraa bot")
                    print("This will cover 4 different subjects, 10 interesting topics with video links for studying.")
                    print("8.Physics")
                    print("9.Chemistry")
                    print("10.Biology")
                    print("11.Mathematics")
                    sub_response = input()
                    if trigger(sub_response, input8):
                        print("Physics:")
                        print("\n\nVideo 1:")
                        print("How Air Expands on Heating?")
                        print("Link: https://youtu.be/mBLSXxh9RKA?list=PL9TTmh_k-_fuVPo7vKHDHI7aT00orpLj3")
                        print("\n\nVideo 2:")
                        print("How does Lightning occur?")
                        print("Link: https://youtu.be/3Scy9g9FgIg?list=PL9TTmh_k-_fuVPo7vKHDHI7aT00orpLj3")

                    elif trigger(sub_response, input9):
                        print("Chemistry: ")
                        print("\n\nVideo 1:")
                        print("Heat")
                        print("Link: https://youtu.be/B3hkpeWC-b8?list=PL9TTmh_k-_fs5Vuc8CJpHpNWOkQVuTIZ2")
                        print("\n\nVideo 2:")
                        print("How is paper made? ")
                        print("Link: https://youtu.be/tDxKWqO1_vU?list=PL9TTmh_k-_fs5Vuc8CJpHpNWOkQVuTIZ2")

                    elif trigger(sub_response, input10):
                        print("Biology: ")
                        print("\n\nVideo 1:")
                        print("Adaptations of Aquatic Animals")
                        print(
                            "Link: https://www.youtube.com/watch?v=APkMeMGppIQ&list=PL9TTmh_k-_fu8urdhQ85VR_FZyTDp7HYU")
                        print("\n\nVideo 2:")
                        print("Tests for Fats")
                        print("Link:  https://youtu.be/RAT5oS-qsaM?list=PL9TTmh_k-_fu8urdhQ85VR_FZyTDp7HYU")

                    elif trigger(sub_response, input11):
                        print("Mathematics: ")
                        print("\n\nVideo 1:")
                        print("Decimals and Fractions")
                        print("Link: https://youtu.be/BVQWJ0POdDE?list=PL9TTmh_k-_fsDrB9vIr8wAykD0QbNVGBR")
                        print("\n\nVideo 2:")
                        print("Congruence of triangles")
                        print("Link: https://youtu.be/Gzkvlv2U7iM?list=PL9TTmh_k-_fsDrB9vIr8wAykD0QbNVGBR")

                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")
                    # user = contact_details()
                    # user.enter_data(user_response)
                    # pickle.dump(user,contacts)

                elif trigger(user_response, input3):
                    print("BOT: ", end="")
                    print(
                        "Eduauraa is your one-stop for the most affordable, comprehensive, and varied educational "
                        "tools required for you to reach your maximum potential.")
                    print("We have the best plans to help you succeed!")
                    print("They are as follows: ")
                    print("\t1. For Classes 6 to 10: Rs 999-/- per year onwards")
                    print("\t2. For Classes 11 / 12: Rs 7999-/- yearly")
                    print("\t3. For JEE - NEET preparation  it is - Rs 11999-/- yearly")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")
                    # user = contact_details()
                    # user.enter_data(user_response)
                    # pickle.dump(user,contacts)

                elif trigger(user_response, input4):
                    print("BOT: ", end="")
                    print(
                        "We believe in sharing is caring. So why not share our love for education with your friends "
                        "and unlock these amazing offers:")
                    print("USE CODE : *100OFF*")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response, input5):
                    print("BOT: ", end="")
                    print(
                        "We would love to connect and hear from our big Eduauraa family! \n To reach out to us find "
                        "us on the following social media platforms: ")
                    print("\n\tTwitter: https://twitter.com/EduauraaTech")
                    print("\tInstagram: https://www.instagram.com/eduauraa/")
                    print("\tFacebook: https://www.facebook.com/eduauraa")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response, input6):
                    print("BOT: ", end="")
                    print(
                        "We are so excited that you have booked a free demo session with us! \n We hope that you "
                        "enjoy our fun learning experience and come back to us for more.")
                    print("\n\n https://www.eduauraa.com/landingpage.html")
                    print("\n\n Our team will get in touch with you soon.")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response, input7):
                    print("BOT: ", end="")
                    print(
                        "We are so sorry for any inconvenience faced. Eduauraa team is here to help you out with any "
                        "queries, questions, or problems that you might have.")
                    print("Please send us your queries at *contact@eduauraa.com* or call us at *18002669990*")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("\tFor iOS: https://cutt.ly/WQHZUrb \n\tFor Android: https://cutt.ly/hQHZG9r")
                    print("\n Reply 0 for going to main menu")
            else:
                clear()
                main_menu()

    else:
        flag = False
        print("BOT: Goodbye!!......")

# In[ ]:
