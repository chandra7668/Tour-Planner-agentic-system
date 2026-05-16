def transport_planner(city, budget):

    if budget.lower() == "low":
        return ["Metro", "Bus"]

    elif budget.lower() == "medium":
        return ["Metro", "Taxi"]

    else:
        return ["Private Cab", "Rental Car"]