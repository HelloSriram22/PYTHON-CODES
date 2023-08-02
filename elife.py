from collections import defaultdict

def assign_rides(rides):
    # Sort rides based on pickup time and price
    sorted_rides = sorted(rides, key=lambda ride: (ride['pickup_time'], ride['price']))

    # Dictionary to store driver assignments
    driver_assignments = defaultdict(list)

    for ride in sorted_rides:
        pickup_time = ride['pickup_time']
        pickup_location = ride['pickup_location']
        drop_off_location = ride['drop_off_location']
        price = ride['price']

        # Find an available driver for the current ride
        assigned_driver = None
        for driver, assigned_rides in driver_assignments.items():
            last_assigned_ride = assigned_rides[-1] if assigned_rides else None

            # Check if there is no conflict and assign the ride to the driver
            if not last_assigned_ride or last_assigned_ride['pickup_time'] <= pickup_time:
                # Check if the driver can preferentially pick up from JFK airport
                if last_assigned_ride and last_assigned_ride['drop_off_location'] == drop_off_location:
                    assigned_driver = driver
                    break
                # If no preference, assign the ride to the driver if they have no previous rides
                if not assigned_driver:
                    assigned_driver = driver

        # Assign the ride to the selected driver
        if assigned_driver:
            driver_assignments[assigned_driver].append(ride)

    return driver_assignments

# Example usage:
rides = [
    {
        'pickup_time': '2023-07-27 09:00',
        'pickup_location': (40.759011, -73.984472),  # Times Square
        'drop_off_location': (40.641311, -73.778139),  # JFK Airport
        'price': 30,
    },
    {
        'pickup_time': '2023-07-27 09:00',
        'pickup_location': (40.758895, -73.985131),  # Times Square
        'drop_off_location': (40.789142, -73.135851),  # Random drop-off location
        'price': 25,
    },
    # Add more rides here
]

driver_assignments = assign_rides(rides)
for driver, assigned_rides in driver_assignments.items():
    print(f"Driver {driver} has been assigned {len(assigned_rides)} rides.")
