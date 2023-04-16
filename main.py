import requests

class CurrencyConverter:
    """
    A simple currency converter class that converts between different currencies using the Exchange Rates API.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.exchangeratesapi.io/latest"

    def convert(self, amount, from_currency, to_currency):
        """
        Convert an amount from one currency to another.
        """
        # Construct the API URL.
        url = f"{self.base_url}?access_key={self.api_key}&base={from_currency}&symbols={to_currency}"

        # Make the API request.
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the response JSON.
            response_json = response.json()

            # Get the exchange rate from the response.
            exchange_rate = response_json["rates"][to_currency]

            # Convert the amount using the exchange rate.
            converted_amount = amount * exchange_rate

            return converted_amount
        else:
            # Handle API errors.
            response.raise_for_status()

# Example usage: convert 100 USD to EUR.
converter = CurrencyConverter(api_key="your_api_key_here")

amount = 100
from_currency = "USD"
to_currency = "EUR"

converted_amount = converter.convert(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
