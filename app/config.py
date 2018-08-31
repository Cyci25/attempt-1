class Config:
    pass

class ProdConfig(Config):
    """docstring for ProdConfig."""
    pass
    # def __init__(self, arg):
    #     super(ProdConfig, self).__init__()
    #     self.arg = arg

class DevConfig(Config):
    DEBUG = True
