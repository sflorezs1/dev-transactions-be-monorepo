# RabbitMQ configuration
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672

# SQLAlchemy configuration
SQLALCHEMY_USERNAME = "postgres"
SQLALCHEMY_PASSWORD = "postgres"
SQLALCHEMY_HOST = "localhost"
SQLALCHEMY_PORT = 5432
SQLALCHEMY_DATABASE = "dt_user"

SQLALCHEMY_DATABASE_URI = f"postgresql+asyncpg://{SQLALCHEMY_USERNAME}:{SQLALCHEMY_PASSWORD}@{SQLALCHEMY_HOST}:{SQLALCHEMY_PORT}/{SQLALCHEMY_DATABASE}"