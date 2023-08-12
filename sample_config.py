# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6671599645:AAEogUro_tkobCzijcsI36GTzm_oV5lU6NY", "")

    APP_ID = os.environ.get("22923523", "")

    API_HASH = os.environ.get("d52c7824d0e66903a0724b800a16ce2c", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("vCuhnUhz5vrqbEakzKujQHpg", "")
