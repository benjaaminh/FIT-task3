import requests
import json
#function that retrieves data from API
def fetch_api_data():
    #api link
    url = "https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/asvu/statfin_asvu_pxt_11x5.px"

#params provided by site https://pxdata.stat.fi/PxWeb/pxweb/sv/StatFin/StatFin__asvu/statfin_asvu_pxt_11x5.px/table/tableViewLayout1/
#(statistikcentralen)
    params= {
  "query": [
    {
      "code": "Alue",
      "selection": {
        "filter": "item",
        "values": [
          "853"
        ]
      }
    },
    {
      "code": "Huoneluku",
      "selection": {
        "filter": "item",
        "values": [
          "01"
        ]
      }
    },
    {
      "code": "Rahoitusmuoto",
      "selection": {
        "filter": "item",
        "values": [
          "2"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "keskivuokra"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}
    #make post request to api url with params
    response = requests.post(url, json=params)

    #response of post request
    results = response.json()

    #years are a list retrieved from response dimension->vuosi->category->label and its values
    years = list(results['dimension']['Vuosi']['category']['label'].values())
    #the values for each year is retrieved from the value array
    values = results['value']

    #data is a list of tuples both of which are the lists of years and values
    data = list(zip(years,values))
    return data