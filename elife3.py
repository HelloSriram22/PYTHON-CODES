import datetime
from collections import defaultdict

def assign_rides(rides, drivers):
    
    # Create a dict to map drivers to their current location and availability
    driver_availability = defaultdict(lambda: {'location': None, 'available_time': datetime.datetime.min})
    
    # Sort rides by pickup time
    rides.sort(key=lambda r: r['pickup_time'])
    
    assigned_rides = []
    
    for ride in rides:
        pickup_time = ride['pickup_time']
        pickup_loc = ride['pickup_loc']
        
        # Find available drivers whose current location is closest to the pickup location
        available_drivers = [d for d in drivers if driver_availability[d]['available_time'] <= pickup_time and
                             distance(driver_availability[d]['location'], pickup_loc) is minimum]
        
        if available_drivers:
            # Assign ride to closest available driver
            driver = available_drivers[0] 
            driver_availability[driver]['location'] = ride['dropoff_loc']
            driver_availability[driver]['available_time'] = pickup_time + ride['duration']
            assigned_rides.append((ride, driver))
        else:
            # No available drivers, skip this ride
            print('No available driver for ride at ', pickup_time)
            
    return assigned_rides