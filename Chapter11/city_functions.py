def city_country(city, country, population="50000"):
    """Generate a neatly formatted city and country"""
    city_details = f"{city}, {country} - population {population}"
    if population:
        city_details = f"{city}, {country} - population {population}"
    else:
        city_details = f"{city}, {country}"

    return city_details.title()


print(city_country("london", "england"))
