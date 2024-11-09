from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv("api_key.env")

# Check if the variables are loaded correctly
api_key = os.getenv("RAPIDAPI_KEY")
api_host = os.getenv("RAPIDAPI_HOST")

# Print to debug
print("API Key:", api_key)
print("API Host:", api_host)
