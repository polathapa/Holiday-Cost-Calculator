def hotel_cost(num_nights):
    # You can customize the hotel cost per night
    return num_nights * 150  # Adjust the cost as needed

def plane_cost(city_flight):
    # Set prices for different cities
    if city_flight == "New York":
        return 500  # Adjust the cost as needed
    elif city_flight == "Paris":
        return 700  # Adjust the cost as needed
    elif city_flight == "Tokyo":
        return 1000  # Adjust the cost as needed
    else:
        return 0  # Default case if city is not recognized

def car_rental(rental_days):
    # You can customize the daily car rental cost
    return rental_days * 50  # Adjust the cost as needed

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Get user inputs
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate costs
hotel_cost_total = hotel_cost(num_nights)
plane_cost_total = plane_cost(city_flight)
car_rental_total = car_rental(rental_days)
total_cost = holiday_cost(hotel_cost_total, plane_cost_total, car_rental_total)

# Print details
print("\nHoliday Details:")
print(f"Flight to {city_flight}: ${plane_cost_total}")
print(f"Hotel stay for {num_nights} nights: ${hotel_cost_total}")
print(f"Car rental for {rental_days} days: ${car_rental_total}")
print("------------------------")
print(f"Total Holiday Cost: ${total_cost}")