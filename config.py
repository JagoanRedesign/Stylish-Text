import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5604388499:AAEttOYuqEIKHWVGr96sLhW0fMr2NTI7rW4")
      API_ID = int(os.environ.get("API_ID", 14962060))
      API_HASH = os.environ.get("API_HASH")
      OWNER_ID = int(os.environ.get("OWNER_ID"))

