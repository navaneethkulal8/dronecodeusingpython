from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative


# Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                    help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

# WE WILL SET THE LATITUDE, LONGITUDE AND ALTITUDE OF 2 WAY POINTS RESPECTIVELY
Latitude_of_waypoint_1 = 0
Latitude_of_waypoint_2 = 0
#DEFINING THE LONGITUDE
Longitude_waypoint_1 = 0
Longitude_waypoint_2 = 0
#DEFINING THE ALTITUDE
Altitude_of_the_drone = 0
# All the condition has been set to zero values will be given according to the mission

# defing the condition of the way point
waypoint1=True
waypoint2=True

# Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()


# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True)


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

if waypoint1=True and waypoint2=True:
    arm_and_takeoff(10)

    print("Set default/target airspeed to 3")
    vehicle.airspeed = 3

    print("Going towards first point for 30 seconds ...")
    point1 = LocationGlobalRelative(Latitude_of_waypoint_1, Longitude_waypoint_1,Altitude_of_the_drone)
    vehicle.simple_goto(point1)

    # sleep so we can see the change in map
    time.sleep(30)

    print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
    point2 = LocationGlobalRelative(Latitude_of_waypoint_2, Longitude_waypoint_2,Altitude_of_the_drone)
    # Vehicle. simple_goto() is the standard DroneKit position controller method. It is called from goto to fly a triangular path.
    vehicle.simple_goto(point2, groundspeed=10)

    # sleep so we can see the change in map
    time.sleep(30)

    #returns to home position.
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")
    break
elif waypoint1 = True:
    # the parameter passed is in m/s
    arm_and_takeoff(10)
    # air speed is the speed with which the drone fly to the waypoint in m/s
    print("Set default/target airspeed to 3")
    vehicle.airspeed = 3

    print("Going towards first point for 30 seconds ...")
    point1 =LocationGlobalRelative(Latitude_of_waypoint_1, Longitude_waypoint_1, Altitude_of_the_drone)#the parameters taken are (lat,lon,alt)   
    vehicle.simple_goto(point1)
    # sleep so we can see the change in map
    time.sleep(30)
    # circular mode code is written below
    print("Going to circular mode")
    vehicle.Mode=VehicleMode("circle mode")
    circle_radius= 3 # in meters
    #returns to home position.
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")
    break
elif waypoint2 = True:
    print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
    point2 = LocationGlobalRelative(Latitude_of_waypoint_2, Longitude_waypoint_2, Altitude_of_the_drone)
    # Vehicle. simple_goto() is the standard DroneKit position controller method. It is called from goto to fly a triangular path.
    vehicle.simple_goto(point2, groundspeed=10)

    # sleep so we can see the change in map
    time.sleep(30)
    print("Going to circular mode")
    vehicle.Mode=VehicleMode("circle mode")
    circle_radius= 3 # in meters
 
    #returns to home position.
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")
    break