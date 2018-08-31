class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=cda6b2edbf2c491d8582d355c7442a3f'

class ProdConfig(Config):
    """docstring for ProdConfig."""
    pass

class DevConfig(Config):
    DEBUG = True
