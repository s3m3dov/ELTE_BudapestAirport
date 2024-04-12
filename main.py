import re
from typing import List, Dict, Union


class BudapestAirport:
    def __init__(self):
        file_name = "input.txt"
        self.data = self.read_input_file(file_name)

    @staticmethod
    def read_input_file(file_name) -> List[Dict[str, Union[str, int]]]:
        with open(file_name, "r") as file:
            _data = []
            lines = file.readlines()
            for line in lines:
                matches = re.match(r'(\S+)\s+(\S+)\s+(\d+)', line)
                if matches:
                    record = {
                        "airline": matches.group(1),
                        "city": matches.group(2),
                        "passengers": int(matches.group(3))
                    }
                    _data.append(record)
            return _data

    @property
    def flights_to_Frankfurt(self) -> int:
        count = 0
        for record in self.data:
            if record["city"] == "Frankfurt":
                count += 1
        return count

    @property
    def flight_with_most_passengers(self) -> str:
        if not self.data:
            return "The file is empty!"
        max_passengers_flight = {}
        for record in self.data:
            if record["passengers"] > max_passengers_flight.get("passengers", 0):
                max_passengers_flight = record

        result = (f"{max_passengers_flight['airline']} {max_passengers_flight['city']} "
                  f"{max_passengers_flight['passengers']}")
        return result

    @property
    def first_flight_with_passengers_less_than_100(self) -> str:
        result = None
        for record in self.data:
            if record["passengers"] < 100:
                result = f"{record['airline']} {record['city']} {record['passengers']}"
                if result:
                    break

        if not result:
            return "There is no flight with passengers less than 100."
        else:
            return result

    @property
    def airline_with_most_passengers(self) -> str:
        if not self.data:
            return "The file is empty!"
        airline_passengers = {}
        for record in self.data:
            airline = record["airline"]
            passengers = record["passengers"]
            airline_passengers[airline] = airline_passengers.get(airline, 0) + passengers

        max_passengers_airline = max(airline_passengers, key=airline_passengers.get)
        return f"{max_passengers_airline} {airline_passengers[max_passengers_airline]}"


if __name__ == "__main__":
    airport = BudapestAirport()
    print(airport.flights_to_Frankfurt)
    print(airport.flight_with_most_passengers)
    print(airport.first_flight_with_passengers_less_than_100)
    print(airport.airline_with_most_passengers)
