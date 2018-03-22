# def bigger(first, second):
#   print(max(first, second))
#   return True
#
# def answer():
#     return 42

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "Введите валидный город !"

def rental_car_cost(days):
    car_rent_pay = days * 40
    if days >= 7:
        return car_rent_pay - 50
    elif days >=3 and days < 7:
        return car_rent_pay - 20
    elif days <3:
        return car_rent_pay
# print(rental_car_cost(3))


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

# print(trip_cost("Tampa", 7))
print(trip_cost("Los Angeles", 5, 600))



