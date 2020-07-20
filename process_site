import requests
from bs4 import BeautifulSoup
import json

prefix = {"author":"Arijit Roy","website":"https://iamarijit.tk","source":"https://www.mygov.in/covid-19"}



def fetchTotalData():

    site = requests.get("https://www.mygov.in/covid-19")

    soup = BeautifulSoup(site.content,'html.parser')

    india_active_case = soup.findAll(class_ = "iblock active-case")[0].findAll(class_="icount")[0].get_text()

    india_recovered = soup.findAll(class_ = "iblock discharge")[0].findAll(class_="icount")[0].get_text()

    india_deaths = soup.findAll(class_ = "iblock death_case")[0].findAll(class_="icount")[0].get_text()

    india_testing_count_till_now = soup.findAll(class_ = "testing_result")[0].findAll(class_ = "testing_count")[0].get_text()

    india_testing_till = soup.findAll(class_ = "testing_result")[0].find("span").get_text().strip("TOTAL SAMPLES TESTED UP TO")

    india_testing_latest_day = soup.findAll(class_ = "testing_sample")[0].findAll(class_ = "testing_count")[0].get_text()

    india_latest_test_day = soup.findAll(class_ = "testing_sample")[0].find("span").get_text().strip("SAMPLES TESTED ON")

    total = [prefix]

    total.append({"active": india_active_case,"recovered": india_recovered,"deaths": india_deaths,"Testing count till now": india_testing_count_till_now,"Latest test date":india_latest_test_day,"Tests on latest day": india_testing_latest_day})

    total = json.dumps(total).strip("[ ]")

    return total


def fetchStatewiseData():

    site = requests.get("https://www.mygov.in/covid-19")

    soup = BeautifulSoup(site.content,'html.parser')

    state_list = soup.find(class_ = "marquee_data view-content").findAll(class_ = "views-row")

    list_statewise = [prefix]

    for i in range(len(state_list)):
        list_statewise.append({
        "state_name":state_list[i].find(class_ ="st_name").get_text(),
        "confirmed": state_list[i].find(class_ ="st_all_counts").find(class_ = "tick-confirmed").find("small").get_text(),
        "active": state_list[i].find(class_ ="st_all_counts").find(class_ = "tick-active").find("small").get_text(),
        "recovered": state_list[i].find(class_ ="st_all_counts").find(class_ = "tick-discharged").find("small").get_text(),
        "death": state_list[i].find(class_ ="st_all_counts").find(class_ = "tick-death").find("small").get_text()
        })

    list_statewise = json.dumps(list_statewise).strip("[]")

    return list_statewise
