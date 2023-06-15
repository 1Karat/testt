#06 04

#vk1.a.gW82_KYzMZhWVTVrgAsaebGSbaPDxbCI9vmxYWKKxN6LutBIdFI-yRwNV6YRLQfCnp-uEkA8_seh_XgttSeNhTzFg2PoAi9dyr3ERi4GU3M3YnNc2XiJQSD3QtBSMpNHBm9PNNadH0YGK0t19xQBhscJr5-QSN-dR_8kNhYTd0ao8uzFYn4mV9ExwRZrQRrRW1V5eqk7ugleC-7tU0P_EA
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
import wiki

TOKEN = "vk1.a.l1kvPh9m7rLZinqEXs4w4lcrEsxvvvX_yT4jVXzv3eXguvzagjIfLACX3X1tWRY5reN30MdlU4ZJRYnBMLWBvQ0a024XkplAVsFUx0igtIl7OFO2fI-hFYqtZgDMzEbtgkndr-cJYwmQULZlhjxizMOT1wlhLUSsFpqP5Zzw8aSkUnRSwIR8cm3-xdmSlbGPJhhTfhBgaVhpBMHysXvXwQ"

vk_session = vk_api.VkApi(token = TOKEN)

# vk_session.method("name_api_method",{"param"})
#переопределения метода запроса
vk = vk_session.get_api()
# vk.name_api_method(params = params)

#подключение longpoll
longpoll = VkLongPoll(vk_session)

#прослушиваем события
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        print(event.type)
        msg = event.text.lower()
        user_id = event.user_id

        random_id = randint(1,10 ** 10)

        if msg == "привет":
            response = "привет"
        elif msg == "пока":
            response = "пока"
        elif msg.startswith("-w"):
            ask = msg[3:]
            response = wiki.get_info_wiki(ask)
        else:
            response = "Такой команды не знаю"
        vk.messages.send( user_id = user_id, random_id = random_id, message = response)








