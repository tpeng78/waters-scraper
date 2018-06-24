import requests
from bs4 import BeautifulSoup

def get_num_pesticide_impaired_waterways(state, url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    events = soup.find('table').findAll('tr')
    pesticides = dict()

    for event in events:
        event_details = dict()

        mycolumns = event.findAll('td')
        if len(mycolumns) == 2: 
            event_details['link'] = event.find('td').find('a')
            if not event_details['link'] is None:
                event_details['name'] = event.find('td').find('a').text
                if not mycolumns[1].get_text() is None: 
                    #print(event_details['name'] + ': ' + mycolumns[1].get_text().strip())
                    pesticides[event_details['name']] = mycolumns[1].get_text().strip()

    
    return pesticides

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
states = ['DC']

state_pesticides = dict()
cycles=[""]
for state in states:
    #print('Pesticide Impairments for State: ' + state)
    cycle='2016'
    pesticides = get_num_pesticide_impaired_waterways(state, 'https://ofmpub.epa.gov/waters10/attains_state.cause_detail_303d?p_cause_group_id=885&p_state=' + state + '&p_cycle=' + cycle + '&p_report_type=')
    state_pesticides[state+str(cycle)]=pesticides

for state in states:
    
    num_incidents = 0
    pesticide_dict = state_pesticides[state]

    #print(pesticide_dict)
    for pesticide_name in pesticide_dict:
        #print(pesticide_name) 
        num_incidents += int(pesticide_dict[pesticide_name])
    if num_incidents > 0: 
        print(state + ' Total Pesticide Imparied Waterways: ' + str(num_incidents))    
    #print(state_pesticides[state])        