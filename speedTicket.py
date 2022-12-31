# Set the speed limits
speed_limit_1 = 60
speed_limit_2 = 80
speed_limit_3 = 120

# Ask the user for the speed of the car
car_speed = int(input("Enter the speed of the car:"))

# Check if the car's speed is over the limits
if car_speed > speed_limit_3:
  # Give a ticket if the speed is over the highest limit
  print("Ticket issued: reckless driving")
elif car_speed > speed_limit_2:
  # Give a ticket if the speed is over the second highest limit
  print("Ticket issued: excessive speeding")
elif car_speed > speed_limit_1:
  # Give a ticket if the speed is over the lowest limit
  print("Ticket issued: speeding")
else:
  # Don't give a ticket if the speed is within all limits
  print("No ticket issued")

