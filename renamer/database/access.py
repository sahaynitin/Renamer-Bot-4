from ..config import Config
from ..database.database import *

clinton = Database(Config.DATABASE_URI, Config.DATABASE_NAME)
