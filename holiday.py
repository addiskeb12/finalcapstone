# this is an example of phyton program showing defining a function 
# function calculate number of nights in the hotel
def hotel_cost(num_nights):
    return num_nights * 45

# option city to visit
def plane_cost(city_flight):
        if city_flight == 'london':
                return 50
        elif city_flight == 'edinburgh':
                return 75
        elif city_flight == 'liverpool':
                return 35
        elif city_flight == 'manchester':
                return 60
        
# daily rental cars cost
def car_rental(rental_days):
    return rental_days * 50

# this function takes 3 argument and produce the total cost of the holiday 
def holiday_cost(num_nights, city_flight, rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

print("Where do you want to spent your holiday?")
 # user select a city to visit        
city_flight = input("London, Edinburgh, Liverpool, Manchester"'\t').lower()                            
# while the city is not one of the 4 cities, keep asking the user
while city_flight not in ["london", "edinburgh", "liverpool", "manchester"]:
            print("Enter the city properly")
            city_flight = input("London, Edinburgh, Liverpool, Manchester"'\t').lower()
try:
    num_nights = int(input("How many nights prefer to stay?" '\t'))
    rental_days = int(input("How many days rent a car?" '\t'))

    print(f"For {num_nights} nights stay at the hotel cost's £{hotel_cost(num_nights)}")    
    print(f"Flight cost £{plane_cost(city_flight)}")
    print(f"For {rental_days } days car rental cost £{car_rental(rental_days)}")
    print(f"You would required a total cost of £{holiday_cost(num_nights,city_flight,rental_days)} to visit {city_flight.capitalize()}")
   
except ValueError:
        print("Please enter the correct number again")









