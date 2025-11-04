#file1 tripdata
def get_trip():
    city = input("Enter city name: ")
    date = input("Enter date visited (dd-mm-yyyy): ")
    comment = input("Enter a short comment: ")
    return {"city": city, "date": date, "comment": comment}


#file2 mainfile
import json
from datetime import datetime
from tripdata import get_trip

trips = []
num = int(input("How many trips do you want to enter? "))

for _ in range(num):
    trip = get_trip()
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")
    trips.append(trip)

json_data = json.dumps(trips, indent=2)
print("\n--- Trip Details in JSON ---")
print(json_data)
