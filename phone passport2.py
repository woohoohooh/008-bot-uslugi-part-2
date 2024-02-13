import pyautogui
import time

ages = [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001]

# STAGE 1 - GETTING DATA FOR INPUT ONE.TXT

# with open('phones.txt', encoding='utf8') as f:
#     print(f.readline(), end='')
#     print(f.readline(), end='')

# with open('one.txt', 'w', encoding='utf8') as f:
#     f.write('')
# with open('two.txt', 'w', encoding='utf8') as f:
#     f.write('')
# with open('three.txt', 'w', encoding='utf8') as f:
#     f.write('')
# with open('four.txt', 'w', encoding='utf8') as f:
#     f.write('')
#
# # click to telegram for checks phone
# pyautogui.moveTo(209, 1058)
# pyautogui.click()
# time.sleep(1)
# pyautogui.write('79513610187')
# time.sleep(1)
# # click to sent
# pyautogui.hotkey('enter')
# time.sleep(8)
# # click to telegram in center
# pyautogui.moveTo(844, 435)
# pyautogui.rightClick()
# time.sleep(1)
# # # copying message
# pyautogui.moveTo(933, 545)
# pyautogui.click()
# time.sleep(1)
# # go to pycharm
# pyautogui.hotkey('alt', 'tab')
# time.sleep(3)
# # click to one.txt
# pyautogui.moveTo(659, 57)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.click()

# STAGE 2 - CHECKS FILE

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
#         age = item2[6:].strip()
#         print(age)
#         if int(age) in ages:
#             d3.append(f'{item1} {item2}')
# print(d3)
#
# with open('two.txt', 'w', encoding='utf8') as f:
#     for i in d3:
#         f.write(i)
#         f.write('\n')
#
# # STAGE 3 - GOING CHECKS IN TELEGRAM FIO+BIRTH DATE
#
# click one.txt for safe datas
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
# pyautogui.moveTo(209, 1058)
# pyautogui.click()
# time.sleep(1)
# # click for write
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
# # click to sent
# pyautogui.hotkey('enter')
# time.sleep(8)
# click to Russia
# pyautogui.moveTo(689, 187)
# pyautogui.click()
# time.sleep(8)

# STAGE 4 - RESULT AFTER INPUT FIO - GOOD OR NO

# # copy result in telegram
# pyautogui.moveTo(847, 904)
# pyautogui.rightClick()
# time.sleep(1)
# pyautogui.moveTo(960, 712)
# pyautogui.click()
# time.sleep(1)
# go pycharm looks result
# pyautogui.hotkey('alt', 'tab')
# time.sleep(1)
# pyautogui.moveTo(876, 65)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)

# STAGE 5 - CKECKS PASSPORT AND COPYING RESULT

# pyautogui.moveTo(875, 60)
# pyautogui.click()
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# with open('four.txt', encoding='utf8') as f:
#     data = f.read()
#     if 'Паспорт' in data:
#         a1 = data.find('Паспорт')
#         e1 = data[a1+9:]
#         e2 = e1[:20]
#         try:
#             b1 = e2.find(',')
#         except:
#             ...
#         if b1 > 0:
#             e3 = e1[:b1].split(',')[0]
#         else:
#             b1 = e2.find('\n')
#             e3 = e1[:b1].split('\n')[0]
#         passport = e3
#     else:
#         print('no')

passport = '8104883370'

# STAGE 6 - GOING CHECK PASSPORT

# pyautogui.moveTo(1222, 63)
# pyautogui.click()
# # go copy result in telegram
# pyautogui.moveTo(209, 1058)
# pyautogui.click()
# time.sleep(1)
# pyautogui.write(f'/passport {passport}')
# time.sleep(1)
# pyautogui.hotkey('enter')
# time.sleep(1)
#  click to file.html
# pyautogui.moveTo(743, 581)
# pyautogui.click()
# time.sleep(1)

# here checks word "Паспорт" and continue after if True
time.sleep(3)
# save file wih passport
pyautogui.moveTo(58, 22)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(145, 163)
pyautogui.click()
time.sleep(1)
pyautogui.write(f'phone passport2')
time.sleep(1)
pyautogui.hotkey('enter')
# click for closest file.html
pyautogui.moveTo(1396, 65)
pyautogui.rightClick()
pyautogui.moveTo(1450, 76)
pyautogui.click()


