import requests
import pandas

def write_to_excel(headers,data, location):
    table_dataframe = pandas.DataFrame(
        data=data, columns=headers)
    table_dataframe.to_excel(location, index=False)  
    

APIKEY = 'c568d0a4'
URL = 'http://www.omdbapi.com/'
query_parameters = {'apikey':APIKEY,'type':'movie','s':'Star Wars','page':1}

response = requests.get(URL,params=query_parameters)
#adding vairable to plug it in the requests for future use

if (response.status_code == 200):
    data = response.json()['Search']
    headers = list(data[0].keys())
    print(data)
    print(headers)
    temp=[]
    for obj in data:
        temp.append(list(obj.values()))
    write_to_excel(headers,data, 'D:\\OMDB_Project.xlsx')
else:
    print(response.reason)


