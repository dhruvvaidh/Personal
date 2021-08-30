#!/usr/bin/env python
# coding: utf-8

# Importing the Libraries

# In[26]:


import numpy as np
import nltk
import string
import random
import re
from os import system, name
#import pickle


# In[27]:


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Importing the corpus

# In[28]:


f = open("chatbot.txt",'r',errors = 'ignore')
raw_doc = f.read()

#Pre Processing and Text Case Handling

raw_doc = raw_doc.lower()#converts everything inside the file into lower case
nltk.download('punkt')# we are going to use punkt tokenizer as it is pre trained for making chatbots.
nltk.download('wordnet')# we are going to use the wordnet dictionary
sent_tokens  = nltk.sent_tokenize(raw_doc)# converts doc into a list of sentences(each element in this list is a sentance)
word_tokens  = nltk.word_tokenize(raw_doc)# converts doc into a list of words(each element in this list is a word)


# Example of Sentence Token

# In[29]:


print(sent_tokens[:2])


# Example of Word Token

# In[30]:


print(word_tokens[:2])


# Text Pre-Processing

# In[31]:


# WordNet dictinary i already included in the nltk library
lemmer = nltk.stem.WordNetLemmatizer()
# WordNet is a semantically-oriented dictionary of English in NLTK
def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]
# We are removing the punctuations from the text here
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Greeting Function

# In[32]:


# this list contains all the possible greetings a user can make to the bot
GREET_INPUTS = ["hello" , "hi" , "greetings" , "sup" , "what's up" , "hey"]
# this list contains some responses the bot can make after the user's greetings 
GREET_OUTPUTS = ["hi" , "hey" , "*nods*" , "hi there" , "hello" , "I'm glad! that you're talking to me"]
pattern = re.compile('|'.join(GREET_INPUTS))
def greet(sentence):
    flag = 0
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            flag = 1
        elif len(re.findall(pattern,word.lower()))>0:
            flag = 1
# When the user enters a sentence, it is being split into words and each is being checked inside the GREET_INPUTS list
    if(flag == 1):
        return random.choice(GREET_OUTPUTS)


# Response Generation

# In[33]:


# We use Text Frequency and Inverse Document Frequency Vectorizer is used to find how many times a term is present in the corpus(Text Frequency)
# Inverse Document Frequency is used to find out how rare a term is in the corpus and it is converted into a vector form which is machine readable

from sklearn.feature_extraction.text import TfidfVectorizer

# After we obtain the the Bag of Words and their correcponding vectors, we use the cosine functionality to give a normalized output

from sklearn.metrics.pairwise import cosine_similarity


# In[34]:


# We are converting the bag of words into vector form so that it is machine readable
# These vectors are converted into matrices which will be used to generate responses
def response(user_response):
  robo1_response = ''
  TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = "english")
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1] , tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if (req_tfidf == 0):
    robo1_response = "I'm Sorry" + "/n" + "I don't understand you"
  else:
    robo1_response = robo1_response + sent_tokens[idx]
    return robo1_response


# Main Menu

# In[35]:


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

# In[36]:


input0 = ['0','back','home','main','refresh','main list']
input1 = ['1','eduauraa information','info','information','about eduauraa','about','boards','board','grade',
          'class','language','english','hindi','marathi']
input2 = ['2','learn','start learning','bot','explain','physics','chemistry','maths','biology']
input3 = ['3','plans','subscribe','subscription','money','pricing']
input4 = ['4','refer & earn','referral program','gifts','rewards','vouchers']
input5 = ['5','social media','facebook','twitter','instagram','linkedin','telegram']
input6 = ['6','live session','trial','book demo','demo','trial','try']
input7 = ['7','customersupport','support','issue','ticket','error','help']
input8 = ['8','physics','phy']
input9 = ['9','chemistry','chem']
input10 = ['10','biology','bio']
input11 = ['11','mathematics','mat','maths']
inputx = ['exit','close','bye','dnd']
def trigger(sentence,inputs):
    pattern = re.compile('|'.join(inputs))
    flag = 0
    for word in sentence.split():
        if word.lower() in inputs:
            flag = 1
        elif len(re.findall(pattern,word.lower()))>0:
            flag = 1
# When the user enters a sentence, it is being split into words and each is being checked inside the GREET_INPUTS list
    if(flag == 1):
        return True
    else:
        return False


# Conversation

# In[37]:


flag = True
print("BOT: ",end="")
print("Hi, \n Welcome to Eduauraa \n We are thrilled to have you aboard \n Lets start your learning experience -")
print("If you want to exit, just type 'Bye'.")
#with open('contact', 'wb') as contacts_file
while (flag==True):
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
    if (trigger(user_response,inputx)==False):
        if (user_response =='thanks' or user_response =='thank you'):
            flag = False
            print("BOT: You are welcome.......")
        else:
            if (greet(user_response) != None):
                print("BOT: "+greet(user_response))
                print("BOT: ",end="\n")
                main_menu()
            if(trigger(user_response,input0)==False):
                if trigger(user_response,input1):
                    print("BOT: ",end="")
                    print("Eduauraa Information")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response,input2):
                    print("BOT: ",end="")
                    print("Learn with Eduauraa bot")
                    print("8.Physics")
                    print("9.Chemistry")
                    print("10.Biology")
                    print("11.Mathematics")
                    sub_response = input()
                    if(trigger(sub_response,input8)):
                        print("Physics Links")
                
                    elif(trigger(sub_response,input9)):
                        print("Chemistry Links")
                    
                    elif(trigger(sub_response,input10)):
                        print("Biology Links")
                    
                    elif(trigger(sub_response,input11)):
                        print("Mathematics Links")
                    
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")
                    #user = contact_details()
                    #user.enter_data(user_response)
                    #pickle.dump(user,contacts)

                elif trigger(user_response,input3):
                    print("BOT: ",end="")
                    print("Subscription Plans")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")
                    #user = contact_details()
                    #user.enter_data(user_response)
                    #pickle.dump(user,contacts)

                elif trigger(user_response,input4):
                    print("BOT: ",end="")
                    print("Refer & Earn")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response,input5):
                    print("BOT: ",end="")
                    print("Social media connect")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response,input6):
                    print("BOT: ",end="")
                    print("Request a live session/demo")
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")

                elif trigger(user_response,input7):
                    print("BOT: ",end="")
                    print("Apologies for the inconvinience caused")
                    print("Please send your query here or you can call at 1800........")
                    query = input().lower()
                    print("\n \n Download the Eduauraa App Now - ")
                    print("Link: ")
                    print("\n Reply 0 for going to main menu")
                else:
                    print("Please try again")
                    user_response = 'bye'
            else:
                clear()
                main_menu()

    else:
        flag = False
        print("BOT: Goodbye!!......")


# In[ ]:




