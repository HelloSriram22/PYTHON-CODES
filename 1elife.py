from datetime import datetime
from collections import defaultdict

# Ride class 
class Ride:
  def __init__(self, id, pickup_time, pickup_loc, pickup_address, dropoff_loc, dropoff_address, duration):
    self.id = id
    self.pickup_time = pickup_time
    self.pickup_loc = pickup_loc
    self.pickup_address = pickup_address
    self.dropoff_loc = dropoff_loc
    self.dropoff_address = dropoff_address
    self.duration = duration

# Driver class
class Driver:
  def __init__(self, id, price_per_mile):
    self.id = id
    self.price_per_mile = price_per_mile
    self.assigned_rides = []

# Sample data
rides = [
  Ride(1, datetime(2023, 7, 28, 9, 0), (40.759011, -73.984472), "Times Square", (40.641311, -73.778139), "JFK Airport", 60),
  Ride(2, datetime(2023, 7, 28, 10, 30), (40.742286, -73.988533), "Madison Square Park", (40.749596, -73.991116), "Penn Station", 20)
]

drivers = [
  Driver("A123", 1.5),
  Driver("B456", 1.2)
]

# Ride assignment function
def assign_rides(rides, drivers):
  
  rides.sort(key=lambda ride: ride.pickup_time)
  
  drivers.sort(key=lambda driver: driver.price_per_mile)

  ride_assignments = defaultdict(list)

  for ride in rides:
   
    for driver in drivers:
      if driver.assigned_rides and driver.assigned_rides[-1].dropoff_loc == ride.pickup_loc:
        ride_assignments[driver].append(ride)
        break
      
    else:
      for driver in drivers:
        if not ride_assignments[driver]:
          ride_assignments[driver].append(ride)
          break

  for driver, assigned_rides in ride_assignments.items():
    driver.assigned_rides.extend(assigned_rides)
  
  return drivers
      
assigned_drivers = assign_rides(rides, drivers)

# Print assigned rides 
print("Ride Assignments:")
for driver in assigned_drivers:
  print(f"Driver {driver.id}")
  for ride in driver.assigned_rides:
    pickup_time = ride.pickup_time.strftime("%H:%M")
    print(f"- {pickup_time} Pickup: {ride.pickup_address}")
    print(f"- Dropoff: {ride.dropoff_address}")
  print()