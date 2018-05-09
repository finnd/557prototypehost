import requests
from bs4 import BeautifulSoup

def pullStatePage(url):
    page = requests.get(url)
    return page

def getCountyLinks(state):
    county_links = []
    page = requests.get(state[1])
    soup = BeautifulSoup(page.content, 'html.parser')
    counties = soup.find('ul', class_='counties list-unstyled row')
    items = counties.find_all('li')
    for item in items:
        county = item.get_text().strip()
        curl = "http://livingwage.mit.edu" + item.find('a')['href']
        county_links.append((county, curl))

    return county_links

def getStateLinks(url):
    state_links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    states = soup.find('ul', class_ = 'states list-unstyled row')
    items = states.find_all('li')
    for item in items:
        state = item.get_text().strip()
        surl = url + item.find('a')['href']
        state_links.append((state, surl))
    return state_links

def getCountyLivingWage(county, state):
    url = county[1]
    url = url.replace("//s", "/s")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all('td')
    
    oneadult = rows[155].get_text().strip().replace("$","").replace(",","")
    oneadultonechild = rows[156].get_text().strip().replace("$", "").replace(",", "")
    oneadulttwochild = rows[157].get_text().strip().replace("$", "").replace(",", "")
    with open (state + "livingwage.txt", 'a') as f:
        f.write(county[0] + "," + oneadult + "," + oneadultonechild + "," + oneadulttwochild + "\n")

def getStateLivingWage(state):
    url = state[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all('td')

    oneadult = rows[155].get_text().strip().replace("$","").replace(",","")
    oneadultonechild = rows[156].get_text().strip().replace("$", "").replace(",", "")
    oneadulttwochild = rows[157].get_text().strip().replace("$", "").replace(",", "")

    with open("allstateslivingwage.txt", 'a') as f:
        f.write(state[0] + "," + oneadult + "," + oneadultonechild + "," + oneadulttwochild + "\n")


if __name__ == "__main__":
    page = pullStatePage("http://livingwage.mit.edu/states/01/locations")
    state_links = getStateLinks("http://livingwage.mit.edu")
##    alabama_links = getCountyLinks(state_links[0])
##    for link in alabama_links:
##        getCountyLivingWage(link, state_links[0][0])

    state_links = list(map(lambda entry: (entry[0], entry[1].replace("/locations", "")), state_links))
    for state in state_links:
        getStateLivingWage(state)
