import requests
from datetime import datetime,timedelta
from flight_data import FlightData

TEQUILA_destination_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_search_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "gZjEeIgxj2LEpZ8nXr2Rk8w34T6d1hCP"




class FlightSearch:

    def get_search(self,destination_city_code,from_time,to_time):
        # from_time = datetime.now()
        # searchtime = from_time + timedelta(days=90)
        headers = {"apikey": TEQUILA_API_KEY}
        search_endpoint = f"{TEQUILA_search_ENDPOINT}/v2/search"
        search_params = {
            "fly_from": "TPE",
            "fly_to":destination_city_code,
            "date_from": from_time, #from_time.strftime("%d/%m/%Y"),   #搜尋開始時間
            "data_to" :to_time, #searchtime.strftime("%d/%m/%Y"),    #搜尋結束時間
            "nights_in_dst_from" : 5, #目的地待最小天數
            "nights_in_dst_to" :5, #目的地待最大天數
            "one_for_city":1,
            "max_stopovers": 1,#中途停靠站
            "curr":"TWD",

        }
        data = requests.get(url=search_endpoint,headers=headers,params=search_params)
        if data.status_code == 200:
            data=data.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("Z")[0],
                out_arrive=data["route"][0]["local_arrival"].split("Z")[0],
                return_date=data["route"][1]["local_departure"].split("Z")[0],
                return_arrive=data["route"][1]["local_arrival"].split("Z")[0],
                airline=data["route"][0]["airline"]+str(data["route"][0]["flight_no"]),
                returnairline = data["route"][1]["airline"] + str(data["route"][1]["flight_no"])
            )
            print(f"{flight_data.destination_city}: NT${flight_data.price}")
            return flight_data
        else:
            print(f"Error {data.status_code}: {data.text}")

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_destination_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term ": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code


