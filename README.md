# Exchange-Rates-API-
Currency Converter ( need to intregate with django web  framework  ) 
In this program, we define a CurrencyConverter class that can be used to convert between different currencies using the Exchange Rates API.

The convert() method takes an amount, a from currency code, and a to currency code as arguments.
It constructs a URL to the Exchange Rates API using the provided API key, base currency, and target currency, and makes an HTTP GET request to the API. 
If the API returns a successful response, the method parses the response JSON to extract the exchange rate for the target currency and uses it to
convert the amount to the target currency.

To use the CurrencyConverter class, we first create an instance of the class using converter = CurrencyConverter(api_key="your_api_key_here").
We can then call the convert() method with an amount, a from currency code, and a to currency code to convert the amount from one currency to another.
The program prints the converted amount to the console.

Note that in order to use this program, you will need to sign up for an API key from Exchange Rates API and replace "your_api_key_here" in the code with
your actual API key.
