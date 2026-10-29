def trip_cost(city, days, spending):
    # 不同城市机票和酒店单价
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


# 调用测试
trip_cost("Los Angeles", 5, 600)
