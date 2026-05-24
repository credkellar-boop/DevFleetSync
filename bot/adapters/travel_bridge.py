from amadeus import Client

# Initialize with credentials from your .env
amadeus = Client(
    client_id='YOUR_AMADEUS_KEY',
    client_secret='YOUR_AMADEUS_SECRET'
)

def search_flights(origin, destination, date):
    """Searches for flight offers."""
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode=origin,
        destinationLocationCode=destination,
        departureDate=date,
        adults=1
    )
    return response.data
