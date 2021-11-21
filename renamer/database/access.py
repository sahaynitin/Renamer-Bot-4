from ..config import Config
from ..database.database import *

clinton = Database(Config.DATABASE_URL, Config.DATABASE_NAME)
