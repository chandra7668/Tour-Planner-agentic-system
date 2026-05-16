def search_hotels(city, budget):

    if budget.lower() == "low":
        return [
            "Budget Inn",
            "Economy Stay",
            "Backpacker Hostel"
        ]

    elif budget.lower() == "medium":
        return [
            "City Hotel",
            "Comfort Suites",
            "Urban Residency"
        ]

    else:
        return [
            "Grand Palace Hotel",
            "Luxury Crown Resort",
            "Elite Residency"
        ]