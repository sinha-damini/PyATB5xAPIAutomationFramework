from dotenv import load_dotenv
import os

# Load .env file explicitly
env_path = "C:\\Users\\HP\\PycharmProjects\\PyATB5xAPIAutomationFramework\\.env"
load_dotenv(env_path, override=True)

print("USERNAME from .env:", os.getenv("USERNAME"))
print("PASSWORD from .env:", os.getenv("PASSWORD"))

# Check if system variables are conflicting
print("System USERNAME:", os.environ.get("USERNAME"))
