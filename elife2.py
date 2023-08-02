import pandas as pd

# Sample data for rides
rides = [
    {
        'pickup_time': '2022-01-01 09:00:00',
        'pickup_location': (40.7589, -73.9851),
        'pickup_address': 'Times Square, New York',
        'dropoff_location': (40.6413, -73.7781),
        'dropoff_address': 'JFK Airport, New York',
        'estimated_duration': 60
    },
    {
        'pickup_time': '2022-01-01 09:00:00',
        'pickup_location': (40.7527, -73.9772),
        'pickup_address': 'Empire State Building, New York',
        'dropoff_location': (40.7128, -74.0060),
        'dropoff_address': 'Wall Street, New York',
        'estimated_duration': 30
    },
    # Add more rides here...
]

# Sort rides by pickup time
rides = sorted(rides, key=lambda x: x['pickup_time'])

# Initialize driver assignments
driver_assignments = {}

# Iterate over rides
for ride in rides:
    pickup_location = ride['pickup_location']
    dropoff_location = ride['dropoff_location']
    
    # Find available drivers
    available_drivers = []
    for driver, assignment in driver_assignments.items():
        if assignment['dropoff_location'] == pickup_location:
            available_drivers.append(driver)
    
    # Sort available drivers by price (lower-priced first)
    available_drivers = sorted(available_drivers, key=lambda x: driver_assignments[x]['price'])
    
    # Assign ride to the first available driver
    if available_drivers:
        driver = available_drivers[0]
        driver_assignments[driver] = {
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'price': ride['estimated_duration']  # Assuming price is based on estimated duration
        }
    else:
        # Assign ride to a new driver
        driver = f'Driver {len(driver_assignments) + 1}'
        driver_assignments[driver] = {
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'price': ride['estimated_duration']  # Assuming price is based on estimated duration
        }

# Print driver assignments
for driver, assignment in driver_assignments.items():
    print(f'{driver}: Pickup from {assignment["pickup_location"]} and dropoff at {assignment["dropoff_location"]}')
