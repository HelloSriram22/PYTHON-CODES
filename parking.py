import json
import random

class ParkingSpot:# This class represents an individual parking spot
    def __init__(self, is_occupied=False, car=None):#this Indicates if the spot is occupied (default is False)
        """Initialize a parking spot.#Holds a reference to the car parked in the spot

        Args:
            is_occupied (bool): Indicates if the spot is occupied.
            car (Car): Reference to the car parked in the spot.
        """
        self.is_occupied = is_occupied
        self.car = car

class ParkingLot:
    def __init__(self, square_footage, parking_spot_size=96):#This class represents the entire parking lot
        """Initialize a parking lot.

        Args:
            square_footage (int): Total square footage of the parking lot.
            parking_spot_size (int): Square footage of each parking spot (default is 96).
        """
        self.parking_spots = [] #A list to store instances of ParkingSpot
        self.num_spots = square_footage // parking_spot_size

        # Create a list of ParkingSpot instances to represent the parking lot
        for i in range(self.num_spots): # the total square footage and the size of each parkingspot 


            self.parking_spots.append(ParkingSpot())

    def get_num_spots(self):#Returns the total number of parking spots in the lot

        """Get the total number of parking spots in the parking lot.

        Returns:
            int: Number of parking spots.
        """
        return self.num_spots

    def is_full(self):
        """Check if the parking lot is full.

        Returns:
            bool: True if all spots are occupied, False otherwise.
        """
        return all(spot.is_occupied for spot in self.parking_spots)

    def park_car(self, car, spot_num):
        """Park a car in a specific spot.#Checks if the spot is valid and unoccupied, then assigns the car to the 

spot.


        Args:
            car (Car): The car to be parked.
            spot_num (int): The spot number where the car will be parked.

        Returns:
            bool: True if the car was parked successfully, False otherwise.
        """
        if spot_num < 0 or spot_num >= self.num_spots:
            return False

        if self.parking_spots[spot_num].is_occupied:
            return False

        self.parking_spots[spot_num].is_occupied = True
        self.parking_spots[spot_num].car = car
        car.park(self, spot_num)
        return True

    def map_vehicles_to_parked_spots(self):
        """Map parked vehicles to their respective spots.

        Returns:
            dict: A dictionary mapping spot numbers to license plates.
        """
        vehicle_map = {}
        for spot_num in range(self.num_spots):
            if self.parking_spots[spot_num].is_occupied:
                vehicle_map[spot_num] = self.parking_spots[spot_num].car.license_plate

        return vehicle_map

class Car:#This class represents a car
    def __init__(self, license_plate):#Holds the license plate of the car
        """Initialize a car.

        Args:
            license_plate (str): The license plate of the car.
        """
        self.license_plate = license_plate
        self.parking_lot = None
        self.spot_num = None

    def __str__(self):
        """Convert the car instance to a string (returns license plate).

        Returns:
            str: The license plate of the car.
        """
        return self.license_plate

    def park(self, parking_lot, spot_num):
        """Assign a car to a parking spot.

        Args:
            parking_lot (ParkingLot): The parking lot where the car is parked.
            spot_num (int): The spot number where the car is parked.
        """
        self.parking_lot = parking_lot
        self.spot_num = spot_num

def main():
    # Create a parking lot with 2000 square feet and 8x12 parking spots
    parking_lot = ParkingLot(2000)

    # Create an array of cars with random license plates
    cars = []
    for i in range(20):
        license_plate = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7))
        cars.append(Car(license_plate))

    # Park the cars in the parking lot until it is full
    while cars and not parking_lot.is_full():
        car = cars.pop()

        # Find a random spot to park the car
        spot_num = random.randint(0, parking_lot.get_num_spots() - 1)

        # Try to park the car in the selected spot
        if parking_lot.park_car(car, spot_num):
            print('Car with license plate {} parked successfully in spot {}'.format(car.license_plate, spot_num))
        else:
            # If the selected spot is occupied, try to find another spot to park the car
            while not parking_lot.park_car(car, spot_num):
                spot_num += 1

                # If the parking lot is full, give up
                if spot_num >= parking_lot.get_num_spots():
                    break

            if spot_num >= parking_lot.get_num_spots():
                print('Car with license plate {} could not find a spot to park in the parking lot.'.format

(car.license_plate))
            else:
                print('Car with license plate {} parked successfully in spot {}'.format(car.license_plate, spot_num))

    # The parking lot is full, exit the program
    print('The parking lot is full.')

    # Save the vehicle map to a JSON file
    vehicle_map = parking_lot.map_vehicles_to_parked_spots()

    with open('vehicle_map.json', 'w') as f:
        json.dump(vehicle_map, f)

if __name__ == '__main__':
    main()
