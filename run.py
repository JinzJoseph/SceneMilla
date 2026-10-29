from app.core.config import get_settings
settings=get_settings()

print(f"App Name: {settings.tavily_api_key}")