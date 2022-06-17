import time

from telethon import TelegramClient, sync

TG_APP_HASH = ''  # api_hash from https://my.telegram.org, under API Development.
TG_APP_ID = 1311864  # also from API Development
haters_id_list = [113347758, ]  # ids of haters


client = TelegramClient('session_name', TG_APP_ID, TG_APP_HASH)
client.start()


while True:
    time.sleep(5)
    for hater_id in haters_id_list:
        for dialog in client.iter_dialogs():
            try:
                if len(client.get_participants(dialog.title)) > 1:
                    for x in client.get_participants(dialog.title):
                        if x.id == hater_id:
                            for message in client.iter_messages(dialog.title, limit=50):
                                if message.sender_id == hater_id:
                                    client.delete_messages(entity=message.peer_id.chat_id, message_ids=message.id)
            except Exception as e:
                pass
