from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
import smtplib
import os
MY_EMAIL = "opmmzxc8612@gmail.com"
sheet = DataManager()
sheet_data = sheet.get_data()
flight_search = FlightSearch()
pprint(sheet_data)

flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])

    sheet.destination_data = sheet_data
    sheet.put_data()
if sheet_data[0]["iataCode"] != "":
    for destination in sheet_data:
        flight = flight_search.get_search(
            destination["iataCode"],destination["from"],destination["to"]
        )
        sheet.update_data(destination["id"],flight.price,flight.out_date,flight.out_arrive,
                          flight.return_date,flight.return_arrive,flight.airline,flight.returnairline)

        MY_PASSWORD = os.getenv("MY_PASSWORD")
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Flight price！\n\n{flight.destination_city}: NT${flight.price}\n{flight.__dict__}".encode('utf-8')
        )




