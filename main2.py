import pyautogui
import time


# ЭТАП 1 - ПОЛУЧЕНИЕ ДАННЫХ И ВСТАВКА В ONE.TXT

# with open('phones.txt', encoding='utf8') as f:
#     print(f.readline(), end='')
#     print(f.readline(), end='')

# # click to telegram
# pyautogui.moveTo(1398, 1055)
# pyautogui.click()
# time.sleep(1)
# # click for write phone
# pyautogui.moveTo(1423, 1000)
# pyautogui.click()
# pyautogui.write('79513610187')
# time.sleep(1)
# # click to sent
# pyautogui.moveTo(1423, 1000)
# pyautogui.click()
# time.sleep(1)
# # click to message
# pyautogui.moveTo(1886, 1005)
# pyautogui.click()
# time.sleep(8)
# # click to pycharm in center
# pyautogui.moveTo(839, 466)
# pyautogui.rightClick()
# time.sleep(1)
# # click to pycharm in panel
# pyautogui.moveTo(1441, 1054)
# pyautogui.click()
# time.sleep(1)
# # click to one.txt
# pyautogui.moveTo(659, 57)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.hotkey('ctrl', 'x')
# pyautogui.click()

# ЭТАП 2 - ОБРАБОТА ФАЙЛА

# pyautogui.moveTo(761, 61)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'a')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'x')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# pyautogui.moveTo(550, 63)
# pyautogui.click()
# time.sleep(1)
#
# with open('one.txt', encoding='utf8') as f:
#     file = f.read()
#
# d1 = []
# a1 = file.find('ФИО')
# e1 = file[a1+5:]
# b1 = e1.find('\n\n')
# c1 = e1[:b1].strip()
# try:
#     c11 = c1.split('\n')
# except:
#     c11 = c1
# for i in c11:
#     d1.append(i)
# print(d1)
#
# d2 = []
# a2 = file.find('🏥 Дата рождения:')
# e2 = file[a2+17:]
# b2 = e2.find(')\n')
# c2 = e2[:b2].strip()
# try:
#     c22 = c2.split(', ')
# except:
#     c22 = c2
# for i in c22:
#     o1 = i.find(' (')
#     o2 = i[:o1].strip()
#     d2.append(o2)
# print(d2)
#
# d3 = []
# for item1 in d1:
#     for item2 in d2:
#         d3.append(f'{item1} {item2}')
# print(d3)
#
# with open('two.txt', 'w', encoding='utf8') as f:
#     for i in d3:
#         f.write(i)
#         f.write('\n')
#
# # ЭТАП 3 - ВСТАВКА СНОВА В ТЕЛЕГРАМ
#
# # click one.txt for safe datas
# pyautogui.moveTo(761, 61)
# pyautogui.click()
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('home')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'up')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'x')
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# # click to telegram
# pyautogui.moveTo(1398, 1055)
# pyautogui.click()
# time.sleep(1)
# # click for write
# pyautogui.moveTo(1423, 1000)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
# # click to sent
# pyautogui.moveTo(1885, 1006)
# pyautogui.click()
# time.sleep(8)
# # click to Russia
# pyautogui.moveTo(689, 187)
# pyautogui.click()
# time.sleep(8)

# appreciate results good or no

# go copy result in telegram
pyautogui.moveTo(1398, 1055)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(847, 904)
pyautogui.rightClick()
time.sleep(1)
pyautogui.moveTo(960, 712)
pyautogui.click()
time.sleep(1)
# go pycharm looks result
pyautogui.moveTo(1357, 1058)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(876, 65)
pyautogui.click()
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
with open('three.txt', encoding='utf8') as f:
    if 'a' in f.read():
        print('yes')
    else:
        print('no')

