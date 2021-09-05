from database import engine,Base
from models import User,Order


Base.metadata.create_all(bind=engine)
