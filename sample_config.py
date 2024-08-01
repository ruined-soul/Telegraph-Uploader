import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7304879730:AAHWnILVrNQjeD7QuLMd3UOuC5xf72mzd5I")

    APP_ID = int(os.environ.get("APP_ID", 2170492))

    API_HASH = os.environ.get("API_HASH", "82b683da442942d5c177ec520318a32f")
