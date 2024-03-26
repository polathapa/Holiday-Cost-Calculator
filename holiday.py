HOTEL_COST_PER_NIGHT = 150
CAR_RENTAL_COST_PER_DAY = 50

def calculate_hotel_cost(num_nights):
    # Calculate the total cost for hotel stay
    return num_nights * HOTEL_COST_PER_NIGHT

def calculate_plane_cost(city_flight_prices):
    # Calculate the cost of the plane ticket based on destination
    if city_flight_prices.get(city_flight):
        return city_flight_prices[city_flight]
    else:
        return 0  # Default case if city is not recognized

def calculate_car_rental_cost(rental_days):
    # Calculate the total cost for car rental
    return rental_days * CAR_RENTAL_COST_PER_DAY

def calculate_total_holiday_cost(hotel_cost, plane_cost, car_rental_cost):
    # Calculate the total holiday cost
    return hotel_cost + plane_cost + car_rental_cost

# Define dictionary of city-flight pairs with corresponding prices
city_flight_prices = {
    "New York": 500,
    "Paris": 700,
    "Tokyo": 1000,
    "Sydney": 1500,
    "Prague": 320,
    "Warsaw": 300,
    "Toronto": 900,
    "Seoul": 1100
}

# Get user inputs
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo, Sydney, Prague, Warsaw, Toronto, Seoul): ")
num_nights = input("Enter the number of nights you will be staying at a hotel: ")
rental_days = input("Enter the number of days for which you will be hiring a car: ")

# Calculate costs
hotel_cost_total = calculate_hotel_cost(num_nights)
plane_cost_total = calculate_plane_cost(city_flight_prices)
car_rental_cost_total = calculate_car_rental_cost(rental_days)
total_cost = calculate_total_holiday_cost(hotel_cost_total, plane_cost_total, car_rental_cost_total)

# Print details
print("\nHoliday Details:")
print(f"Flight to {city_flight}: ${plane_cost_total}")
print(f"Hotel stay for {num_nights} nights: ${hotel_cost_total}")
print(f"Car rental for {rental_days} days: ${car_rental_cost_total}")
print("------------------------")
print(f"Total Holiday Cost: ${total_cost}")
