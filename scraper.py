import requests
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    events = soup.find('table').findAll('tr')
    #print(events[0])
    for event in events:
        event_details = dict()
        #print('\n\n' + str(event.findAll('td')))
        mycolumns = event.findAll('td')
        if len(mycolumns) == 2: 
            #print(str(len(mycolumns)))
            event_details['link'] = event.find('td').find('a')
            if not event_details['link'] is None:
                event_details['name'] = event.find('td').find('a').text
                #print(event_details['name'])
                #print(mycolumns[1])
                if not mycolumns[1].get_text() is None: 
                    print(event_details['name'] + ': ' + mycolumns[1].get_text().strip())
            #event_details['location'] = event.find('span', {'class', 'event-location'}).text
            #event_details['time'] = event.find('time').text
            

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
states = ['DC','TX']

for state in states:
    print('Pesticide Impairments for State: ' + state)
    get_upcoming_events('https://ofmpub.epa.gov/waters10/attains_state.cause_detail_303d?p_cause_group_id=885&p_state=' + state + '&p_cycle=2014&p_report_type=')