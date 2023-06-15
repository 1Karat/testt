
import vk_api


TOKEN= "vk1.a.l1kvPh9m7rLZinqEXs4w4lcrEsxvvvX_yT4jVXzv3eXguvzagjIfLACX3X1tWRY5reN30MdlU4ZJRYnBMLWBvQ0a024XkplAVsFUx0igtIl7OFO2fI-hFYqtZgDMzEbtgkndr-cJYwmQULZlhjxizMOT1wlhLUSsFpqP5Zzw8aSkUnRSwIR8cm3-xdmSlbGPJhhTfhBgaVhpBMHysXvXwQ"




vk = vk_api.VkApi(token = TOKEN)
vk._auth_token() # авторизация токена

#делаю запрос и получаю ответ
message = vk.method(
                    "messages.getConversations",
                    {"count":20,'filter':'unanswered' }
                    )
#вывожу ответ




user_id = message['items'][0]["last_message"]['from_id']        #id пользователя
text_msg = message['items'][0]["last_message"]['text']          #сообщение
message_id = message['items'][0]["last_message"]['id']          #id сообщение

vk.method(
        "messages.send",  #отправляем сообщение
        {
            "peer_id"  : user_id,
            'random_id': message_id,
            'message'  : "BMW или Mersedes"
        }
        )












