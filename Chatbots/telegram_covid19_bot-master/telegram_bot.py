from telegram.ext import Updater, CommandHandler
import requests

def get_state_district_wise_data(state,city):
    url = 'https://api.covid19india.org/v2/state_district_wise.json'
    r = requests.get(url)
    state_district_data = r.json()
    for data in state_district_data:
        if data["state"].lower() == state.lower():
            dictrictData = data["districtData"]
            for district in dictrictData:
                if(district["district"].lower() == city.lower()):
                    return district

def tweet_city_status(state,city):
    selected_city_data = get_state_district_wise_data(state,city)
    active_cases = selected_city_data["active"]
    confirmed_cases = selected_city_data["confirmed"]
    deceased_cases = selected_city_data["deceased"]
    recovered_cases = selected_city_data["recovered"]
    tweet = f"Status Update For {city}, {state}"
    tweet += f"\n No. of Active Cases: {active_cases}" 
    tweet += f"\n No. of Confirmed Cases: {confirmed_cases}" 
    tweet += f"\n No. of Deceased Cases: {deceased_cases}" 
    tweet += f"\n No. of Recovered Cases: {recovered_cases}"
    #print(tweet)
    return(tweet)

def get_resources_information(state,city):
    url = 'https://api.covid19india.org/resources/resources.json'
    r = requests.get(url)
    resources = r.json()["resources"]
    state_resources = []
    for data in resources:
        if data["state"].lower() == state.lower() and data["city"].lower() == city.lower():
            state_resources.append(data)
    return state_resources

def segregate_resources(state,city,isGetCategories=False):
    selected_city_resources = get_resources_information(state,city)
    resource_dictionary = {}
    for resource in selected_city_resources:
        if resource["category"] in resource_dictionary:
            resource_dictionary[resource["category"]].append(resource)
        else:
            resource_dictionary[resource["category"]] = [resource]
    if isGetCategories:
        category_dict = {}
        values = resource_dictionary.keys()
        i = 0
        for value in values:
            category_dict[str(i)] = value
            i += 1
        return category_dict
    return resource_dictionary

def tweet_resources(state,city,selected_category):
    resources = segregate_resources(state,city)[selected_category]
    tweet = city
    i = 1
    for resource in resources:
        organization_name = resource["nameoftheorganisation"]
        #description_of_services = resource["descriptionandorserviceprovided"]
        phone_number = resource["phonenumber"]
        #url = resource["contact"]
        tweet += f"\n{i}. Organization Name: {organization_name}"
        #if description_of_services != "":
        #    tweet += f"\n Description of service: {description_of_services}"
        if phone_number != "":
            tweet += f"\n Phone Number: {phone_number}\n"
        #if url != "":
        #    tweet += f"\n URL: {url}\n\n"
        i += 1
    #print(tweet)
    return tweet
    

def start(bot, update):
    text = "CLICK ON THE NUMBER FOR DETAILS\n\n/1 - Latest Covid 19 Mumbai Numbers\n\n/2 - Accommodation Help\n\n/3 - Food Delivery\n\n/4 - Covid Testing Centers\n\n/5 - Free Food\n\n/6 - Fundraiser\n\n/7 - Domestic Violence\n\n/8 - Helpline Numbers"
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    
def latest(bot, update):
    text = tweet_city_status("Maharashtra","Mumbai")
    text2 = tweet_city_status("Maharashtra","Thane")
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    bot.send_message(chat_id = chat_id, text = text2)

def resource_accommodation(bot, update):
    text = "Accommodation details are provided in the document below\n\nhttp://tiny.cc/aiwdoz"
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    bot.send_document(chat_id = chat_id, document = "https://drive.google.com/open?id=1tvTx1gIPR0gt4PydUd_kUdlOjjR_-XWx")
    
def resource_food_delivery(bot, update):
    text = tweet_resources("Maharashtra","Mumbai","Delivery [Vegetables, Fruits, Groceries, Medicines, etc.]")
    text2 = tweet_resources("Maharashtra","Thane","Delivery [Vegetables, Fruits, Groceries, Medicines, etc.]")
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    bot.send_message(chat_id = chat_id, text = text2)

def resource_covid19_testinglab(bot, update):
    text = tweet_resources("Maharashtra","Mumbai","CoVID-19 Testing Lab")
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)

def resource_freefood(bot, update):
    text = tweet_resources("Maharashtra","Mumbai","Free Food")
    text2 = tweet_resources("Maharashtra","Thane","Free Food")
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    bot.send_message(chat_id = chat_id, text = text2)

def resource_fundraiser(bot, update):
    text = tweet_resources("Maharashtra","Mumbai","Fundraisers")
    text2 = tweet_resources("Maharashtra","Navi Mumbai","Fundraisers")
    text3 = tweet_resources("Maharashtra","Thane","Fundraisers")
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    bot.send_message(chat_id = chat_id, text = text2)
    bot.send_message(chat_id = chat_id, text = text3)

def resource_domestic_violence(bot, update):
    text = tweet_resources("Maharashtra","Mumbai","Other")
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)
    
def resource_helpline_number(bot, update):
    text = "Helpline Numbers\n\nMumbai Police - 9867097665\n\nBMC emergency helpline - 1916\n\nBMC Helpline to get tested - 2247085085\n\nTMC Corona (Covid-19) Prevention helpline number - 1800222108\n\nImportant Helplines for Women facing Domestic Violence - 9029073154/7506732641/8928585479"
    chat_id = update.message.chat_id
    #print(text)
    bot.send_message(chat_id = chat_id, text = text)

def main():
    updater = Updater('1201430678:AAFWyf2IK2apkJ1vqpopUh3-GaMzNZ6WMK4')
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('menu',start))
    dp.add_handler(CommandHandler('1',latest))
    dp.add_handler(CommandHandler('2',resource_accommodation))
    dp.add_handler(CommandHandler('3',resource_food_delivery))
    dp.add_handler(CommandHandler('4',resource_covid19_testinglab))
    dp.add_handler(CommandHandler('5',resource_freefood))
    dp.add_handler(CommandHandler('6',resource_fundraiser))
    dp.add_handler(CommandHandler('7',resource_domestic_violence))
    dp.add_handler(CommandHandler('8',resource_helpline_number))
    
    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    main()