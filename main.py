import vk_api, base, sqlite3
import function as f
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
# индефикатор сообщества
token = "access token"
# индефикация переменных
vk_session = vk_api.VkApi(token = token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
# клавиаткра
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Добавить', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('Удалить', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Календарь', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Парсер', color=VkKeyboardColor.POSITIVE)
# Старт лонгпола
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            base.check(event.user_id)# Проверка регистрации пользователя
            if event.text.lower() == 'календарь':
                cal = base.mas(event.user_id)
                cal_l = 0
                for i in cal:
                    cal_l+=1
                    cal_l = str(cal_l)
                    i = cal_l +'.'+ i
                    cal_l = int(cal_l)
                    vk.messages.send(
                        user_id=event.user_id,
                        message = i,
                        keyboard = keyboard.get_keyboard(),
                        random_id=get_random_id(),
                    )
            if event.text.lower() == 'начать':
                vk.messages.send(
                    user_id=event.user_id,
                    message = ' добавить - новая ячейка в вашем списке, удалить - удолить из списка, календарь - список, парсер- информация со стены групп',
                    keyboard = keyboard.get_keyboard(),
                    random_id=get_random_id(),
                )
            elif event.text.lower() == 'парсер':
                vk.messages.send(
                    user_id=event.user_id,
                    message = 'Введите имя группы',
                    random_id=get_random_id(),
                )
                base.group_name(event.user_id)
            elif event.text.lower() == 'добавить':
                print('Добавть прошли')
                vk.messages.send(
                    user_id=event.user_id,
                    message='Введите мероприятие в виде (дата)(врема): событие, дата вводится, например так 12.12.2020',
                    random_id=get_random_id(),
                )
                base.add_tru(event.user_id)
            elif event.text.lower() == 'удалить':
                vk.messages.send(
                    user_id=event.user_id,
                    message='Введите номер события',
                    random_id=get_random_id(),
                )
                base.del_tru(event.user_id)
            elif event.text.lower() == 'начать':
                vk.messages.send(
                    user_id=event.user_id,
                    message='Хай',
                    keyboard = keyboard.get_keyboard(),
                    random_id=get_random_id(),
                )
            else:
                text = base.cl(event.text)
                if base.add_pr(event.user_id) == str(1):
                    print('2 у словие добавить')
                    base.add(event.user_id, 'all_date', text)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Мероприятие успешно добавлено!!!',
                        random_id=get_random_id(),
                    )
                    base.add_off(event.user_id)
                elif base.group_name_pr(event.user_id) == str(1):
                    try:
                        a = f.parser_wall_text(event.text)
                        b = f.parser_wall_img(event.text)
                        for j in range(5):
                            vk.messages.send(
                                user_id=event.user_id,
                                message= a[j],
                                random_id=get_random_id(),
                            )
                            vk.messages.send(
                                user_id=event.user_id,
                                message= b[j],
                                random_id=get_random_id(),
                            )
                        base.group_name_off(event.user_id)
                    except KeyError:
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Неверный адрес',
                            random_id=get_random_id(),
                        )
                        base.group_name_off(event.user_id)
                elif base.del_pr(event.user_id) == str(1):
                    try:
                        base.delete(event.user_id, base.mas, int(text)-1,'all_date')
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Мероприятие успешно удалено!!!',
                            random_id=get_random_id(),
                        )
                        base.del_off(event.user_id)
                    except IndexError:
                        vk.messages.send(
                            user_id=event.user_id,
                            message='У вас нет событий с таким индексом',
                            random_id=get_random_id(),
                        )
                        base.del_off(event.user_id)
                    except ValueError:
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Цифры необходимо вводить',
                            random_id=get_random_id(),
                        )
                        base.del_off(event.user_id)
