departure_time = input("Enter the departure time (HH:MM): ")
departure_hour, departure_minute = map(int, departure_time.split(':'))

arrival_time = input("Enter the arrival time (HH:MM): ")
arrival_hour, arrival_minute = map(int, arrival_time.split(':'))

trip_hour = arrival_hour - departure_hour
trip_minute = arrival_minute - departure_minute

if trip_minute < 0:
    trip_hour -= 1
    trip_minute += 60

print(f"Trip time: {trip_hour} hr and {trip_minute} min")
