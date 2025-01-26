import requests




class DataManager:
    def __init__(self):
        self.base_url = "https://api.sheety.co/6487a580ba1b9e75cda6337883829986/flightDeals/prices"
        self.put_url = "https://api.sheety.co/6487a580ba1b9e75cda6337883829986/flightDeals/prices/Flight Deals"
        self.response = None

    def get_data(self):
        self.response = requests.get(url=self.base_url)
        if self.response.status_code == 200:
            self.destination_data = self.response.json()["prices"]
            return self.destination_data
        else:
            print(f"Error {self.response.status_code}: {self.response.text}")
            return None

    def put_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.base_url}/{city['id']}",  #抓id(row)
                json=new_data
            )
            print(response.text)
        if self.response.status_code == 200:
            print("success")
        else:
            print(f"Error {self.response.status_code}: {self.response.text}")
            return None

    def update_data(self,id,price,out_time,out_arrive,return_time,return_arrive,airline,returnairline):
        new_data = {
                "price": {
                    "lowestPrice" : price,
                    "out(de)" : out_time,
                    "out(arrive)" : out_arrive,
                    "return(de)" : return_time,
                    "return(arrive)" : return_arrive,
                    "airline" : airline,
                    "returnairline" : returnairline
                }
            }
        response = requests.put(
                url=f"{self.base_url}/{id}",  #抓id(row)
                json=new_data
            )
        print(response.text)
        if self.response.status_code == 200:
            print("success")
        else:
            print(f"Error {self.response.status_code}: {self.response.text}")
            return None
