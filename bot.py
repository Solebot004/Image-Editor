# By @TroJanzHEX
from pyrogram import Client
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from sample_config import Config  # pylint:disable=import-error


if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "lisa",
        bot_token='6671599645:AAEogUro_tkobCzijcsI36GTzm_oV5lU6NY',
        api_id='22923523',
        api_hash='d52c7824d0e66903a0724b800a16ce2c',
        plugins=plugins,
        workers=300,
    )
    app.run()
