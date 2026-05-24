# bot/adapters/mobility_bridge.py
import requests

class MobilityBridge:
    def __init__(self, api_key):
        self.base_url = "https://api.aggregator-example.com/v1" # Use your chosen MaaS provider
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def search_transport(self, lat, lon, transport_type):
        """
        transport_type: 'ride' (Uber/Lyft/Waymo) or 'rental' (Hertz/Enterprise/Turo)
        """
        endpoint = f"{self.base_url}/search"
        params = {"lat": lat, "lon": lon, "type": transport_type}
        
        response = requests.get(endpoint, headers=self.headers, params=params)
        return response.json()

    def book_transport(self, provider_id, vehicle_id):
        # Unified booking call
        endpoint = f"{self.base_url}/book"
        data = {"provider": provider_id, "id": vehicle_id}
        
        return requests.post(endpoint, headers=self.headers, json=data).json()
