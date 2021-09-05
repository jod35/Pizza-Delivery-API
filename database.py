from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:nathanoj35@localhost/pizza_delivery',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()