import sqlite3

def add(user_id, day ,message):# запись события
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    old_text = curs.execute(f"SELECT all_date FROM users WHERE id_vk = {user_id}")
    curs.execute(f"UPDATE users SET all_date = '{str(old_text.fetchone()[0])+'{'+message+'}'}' WHERE id_vk = {user_id}")
    db.commit()

def check(user_id): # проверка пользователя
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    curs.execute('SELECT id_vk FROM users')
    a = curs.fetchall()
    a_bul = True
    user = str(user_id)
    for i in range(len(a)):
        if user == str(a[i][0]):
            a_bul = False
            break
    if a_bul == True:
        curs.execute(f"INSERT INTO users VALUES (?,?,?,?,?)",(user,'0','{Это блокнот}','0', '0'))
        db.commit()


def mas(user_id):# обработка строки
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    curs.execute(f"SELECT all_date FROM users WHERE id_vk = {user_id}")
    curs_fetch = curs.fetchone()
    masiv = []
    barier = ''
    j = 0
    for i in curs_fetch[0]:
        barier = barier + i
        if i == '}':
            masiv.append(barier)
            barier = ''
    return(masiv)

def delete(user_id,mas, number, day):# удаление записи
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    masiv = mas(user_id)
    masiv.pop(number)
    bar = ''
    for i in masiv:
        bar = bar + i
    curs.execute(f"UPDATE users SET {day} = '{bar}' WHERE id_vk = {user_id}")
    db.commit()


def add_tru(user_id):# вес для add
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"UPDATE users SET plus = '1' WHERE id_vk = {user}")
    db.commit()

def del_tru(user_id): # вес для delete
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"UPDATE users SET minus = '1' WHERE id_vk = {user}")
    db.commit()

def add_pr(user_id): # проверка add
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"SELECT plus FROM users WHERE id_vk = {user}")
    curs_fetch = str(curs.fetchone()[0])
    return curs_fetch

def add_off(user_id): # обнуления веса add
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    a = str(1)
    user = str(user_id)
    curs.execute(f"UPDATE users SET plus = '0' WHERE id_vk = {user}")
    db.commit()

def del_pr(user_id):# проверка веса delete
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"SELECT minus FROM users WHERE id_vk = {user}")
    curs_fetch = str(curs.fetchone()[0])
    return curs_fetch

def del_off(user_id):# обнуление веса delete
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"UPDATE users SET minus = '0' WHERE id_vk = {user}")
    db.commit()

def cl(message):# переназначение скобок
    a = ''
    for i in message:
        if i == '{':
            i = '('
        elif i == '}':
            i = ')'
        a+=i
    return a

def group_name(user_id):# вес для group
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"UPDATE users SET group_name = '1' WHERE id_vk = {user}")
    db.commit()

def group_name_pr(user_id): # проверка веса group
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"SELECT group_name FROM users WHERE id_vk = {user}")
    curs_fetch = str(curs.fetchone()[0])
    return curs_fetch

def group_name_off(user_id): # обнуление веса group
    db = sqlite3.connect('db.db')
    curs = db.cursor()
    user = str(user_id)
    curs.execute(f"UPDATE users SET group_name = '0' WHERE id_vk = {user}")
    db.commit()
