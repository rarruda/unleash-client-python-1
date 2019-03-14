from .UnleashClient import UnleashClient

client = UnleashClient("https://unleash.herokuapp.com/api", "My Program")
client.initialize_client()


app_context = {"userId": "test@email.com"}
result = client.is_enabled("User ID Toggle", app_context)

print("result is: {result}")
