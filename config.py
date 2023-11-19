from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "60ad9e3ddf5457d5fac68611e0fed61c")
      API_ID = int(getenv("API_ID", "26147784"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6577337183:AAFv1de-DNPIeeL6lsTz0xufoKrnm3XSIcw")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1887377952:-1888470782").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
