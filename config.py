class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Evita warning innecesario
    SECRET_KEY = "secret-key"