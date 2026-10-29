def trip_cost(city, days, spending):
    if city == "Los Angeles":
        flight = 475
        hotel_per_day = 148
    elif city == "Chicago":
        flight = 250
        hotel_per_day = 125
    elif city == "New York":
        flight = 400
        hotel_per_day = 200
    else:
        flight = 0
        hotel_per_day = 0

    total = flight + hotel_per_day * days + spending
    print(total)
    return total


trip_cost("Los Angeles", 5, 600)
