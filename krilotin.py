# #11
# """word = str(input("enter the word: "))
# lotincha = {
#     'й': 'y',
#     'ҳ': 'h',
#     'қ': 'q',
#     'ў': "o'",
#     'ғ': "g'",
#     'y': 'u',
#     'к': 'k',
#     'н': 'n',
#     'г': 'g',
#     'ш': 'sh',
#     'щ': 'sh',
#     'з': 'z',
#     'ф': 'f',
#     'в': 'v',
#     'а': 'a',
#     'п': 'p',
#     'р': 'r',
#     'о': 'o',
#     'л': 'l',
#     'д': 'd',
#     'ч': 'ch',
#     'с': 's',
#     'м': 'm',
#     'и': 'i',
#     'т': 't',
#     'б': 'b',
#     'ж': 'j',
#     'е': 'e',
#     'э': 'e',
#     'х': 'x',
#     'Ъ': "'",
#     'я': 'ya',
#     'ю': 'yu',
#     'ы': 'i',
#     ' ': ' ',
#     'ё': 'yo'
#      }
# lotincha_katta = {
#     'Й': 'Y',
#     'Ё': 'Yo',
#     'Ғ': "G'",
#     'Ў': "O'",
#     'Қ': 'Q',
#     'Ҳ': 'H'
#     'У': 'U',
#     'К': 'K',
#     'Н': 'N',
#     'Г': 'G',
#     'Ш': 'SH',
#     'Щ': 'SH',
#     'З': 'Z',
#     'Ф': 'F',
#     'В': 'V',
#     'А': 'A',
#     'П': 'P',
#     'Р': 'R',
#     'О': 'O',
#     'Л': 'L',
#     'Д': 'D',
#     'Ч': 'CH',
#     'С': 'S',
#     'М': 'M',
#     'И': 'I',
#     'Т': 'T',
#     'Б': 'B',
#     'Ж': 'J',
#     'Е': 'E',
#     'Э': 'E',
#     'Х': 'X',
#     'Ъ': "'",
#     'Я': 'Ya',
#     'Ю': 'Yu',
#     'Ы': 'I',
#     ' ': ' '
#      }
#
# new_word = ''
# for i in range(0,len(word)):
#     if word[i].lower() == word[i]:
#         if i == 0 and word[i] == 'ц':
#             new_word += 's'
#         else:
#             if word[i]=='ц':
#                     if word[i-1]==' ':
#                         new_word += 's'
#                     else:
#                         new_word+='ts'
#             for j in lotincha:
#
#                 if word[i] == j:
#                     new_word += lotincha[j]
#     else:
#         if i == 0 and word[i] == 'Ц':
#             new_word += 'S'
#         else:
#             if word[i]=='Ц':
#                     if word[i-1]==' ' or '':
#                         new_word += 'S'
#                     else:
#                         new_word+='TS'
#             for j in lotincha_katta:
#
#                 if word[i] == j:
#                     new_word += lotincha_katta[j]
# print(new_word)"""
# #12
# word = str(input("enter the word: "))
# lotincha = {
#     'й': 'y',
#     'ҳ': 'h',
#     'қ': 'q',
#     'ў': "o'",
#     'ғ': "g'",
#     'y': 'u',
#     'к': 'k',
#     'н': 'n',
#     'г': 'g',
#     'ш': 'sh',
#     'щ': 'sh',
#     'з': 'z',
#     'ф': 'f',
#     'в': 'v',
#     'а': 'a',
#     'п': 'p',
#     'р': 'r',
#     'о': 'o',
#     'л': 'l',
#     'д': 'd',
#     'ч': 'ch',
#     'с': 's',
#     'м': 'm',
#     'и': 'i',
#     'т': 't',
#     'б': 'b',
#     'ж': 'j',
#     'е': 'e',
#     'э': 'e',
#     'х': 'x',
#     'Ъ': "'",
#     'я': 'ya',
#     'ю': 'yu',
#     ' ': ' ',
#     'ё': 'yo'
# }
#
# lotincha_katta = {
#     'Й': 'Y',
#     'Ё': 'Yo',
#     'Ғ': "G'",
#     'Ў': "O'",
#     'Қ': 'Q',
#     'Ҳ': 'H',
#     'У': 'U',
#     'К': 'K',
#     'Н': 'N',
#     'Г': 'G',
#     'Ш': 'SH',
#     'Щ': 'SH',
#     'З': 'Z',
#     'Ф': 'F',
#     'В': 'V',
#     'А': 'A',
#     'П': 'P',
#     'Р': 'R',
#     'О': 'O',
#     'Л': 'L',
#     'Д': 'D',
#     'Ч': 'CH',
#     'С': 'S',
#     'М': 'M',
#     'И': 'I',
#     'Т': 'T',
#     'Б': 'B',
#     'Ж': 'J',
#     'Е': 'E',
#     'Э': 'E',
#     'Х': 'X',
#     'Ъ': "'",
#     'Я': 'Ya',
#     'Ю': 'Yu',
#     ' ': ' '
# }
# incorrect_words = {
# 'целлофан': 'sellofan',
# 'целлюлоза': 'sellyuloza',
# 'цельсий': 'selsiy',
# 'цемент': 'sement',
# 'цензор': 'senzor',
# 'цензура': 'senzura',
# 'центнер': 'sentner',
# 'цех': 'sex',
# 'цеце': 'setse',
# 'цивилизация': 'sivilizatsiya',
# 'цикл': 'sikl',
# 'циклон': 'siklon',
# 'циклоп': 'siklop',
# 'цилиндр': 'silindr',
# 'цилиндрик': 'silindrik',
# 'цилиндрсимон': 'silindrsimon',
# 'цирк': 'sirk',
# 'циркуль': 'sirkul',
# 'цистерна': 'sisterna',
# 'цитрус': 'sitrus'
# }
# if word in incorrect_words.values():
#     for i in incorrect_words:
#         if word == incorrect_words[i]:
#             print(i)
#             break
# else:
#     new_word = ''
#     i = 0
#     while i < len(word):
#         if word[i].lower() == word[i]:
#             if word[i:i+2] in ('sh', 'ch', "o'", "g'", 'yo', 'ya', 'yu', 'ts'):
#                 if word[i:i+2] == 'sh':
#                     new_word += 'ш'
#                     i += 2
#                 elif word[i:i+2] == 'ch':
#                     new_word += 'ч'
#                     i += 2
#                 elif word[i:i+2] == "o'":
#                     new_word += 'ў'
#                     i += 2
#                 elif word[i:i+2] == "g'":
#                     new_word += 'ғ'
#                     i += 2
#                 elif word[i:i+2] == 'ts':
#                     new_word += 'ц'
#                     i += 2
#                 elif word[i:i+2] == 'yo':
#                     new_word += 'ё'
#                     i += 2
#                 elif word[i:i+2] == 'ya':
#                     new_word += 'я'
#                     i += 2
#                 elif word[i:i+2] == 'yu':
#                     new_word += 'ю'
#                     i += 2
#             else:
#                 if i == 0 and word[i] == 'e':
#                     new_word += 'э'
#                     i += 1
#                 else:
#                     if word[i] == 'e':
#                         if word[i-1] == ' ':
#                             new_word += 'э'
#                         else:
#                             new_word += 'е'
#                     else:
#                         for j in lotincha:
#                             if word[i] == lotincha[j]:
#                                 new_word += j
#                         i += 1
#         else:
#             if word[i:i+2] in ('SH', 'Ch', "O'", "G'", 'Yo', 'Ya', 'Yu', 'Ts', 'Sh', 'Ch', 'YO', 'YU', 'YA', 'TS'):
#                 if word[i:i+2] == 'SH' or word[i:i+2] == 'Sh':
#                     new_word += 'Ш'
#                     i += 2
#                 elif word[i:i+2] == 'Ch' or word[i:i+2] == 'CH':
#                     new_word += 'Ч'
#                     i += 2
#                 elif word[i:i+2] == "O'":
#                     new_word += 'Ў'
#                     i += 2
#                 elif word[i:i+2] == "G'":
#                     new_word += 'Ғ'
#                     i += 2
#                 elif word[i:i+2] == 'TS' or word[i:i+2] == 'Ts':
#                     new_word += 'Ц'
#                     i += 2
#                 elif word[i:i+2] == 'Yo' or word[i:i+2] == 'YO':
#                     new_word += 'Ё'
#                     i += 2
#                 elif word[i:i+2] == 'Ya' or word[i:i+2] == 'YA':
#                     new_word += 'Я'
#                     i += 2
#                 elif word[i:i+2] == 'Yu' or word[i:i+2] == 'YU':
#                     new_word += 'Ю'
#                     i += 2
#             else:
#                 if i == 0 and word[i] == 'E':
#                     new_word += 'Э'
#                 else:
#                     if word[i] == 'E':
#                         if word[i-1] == ' ':
#                             new_word += 'Э'
#                         else:
#                             new_word += 'E'
#                     else:
#                         for j in lotincha_katta:
#                             if word[i] == lotincha_katta[j]:
#                                 new_word += j
#                         i += 1
#
#     print(new_word)




word = str(input("enter the word: "))
lotincha = {
    'й': 'y',
    'ҳ': 'h',
    'қ': 'q',
    'ў': "o'",
    'ғ': "g'",
    'у': 'u',
    'к': 'k',
    'н': 'n',
    'г': 'g',
    'ш': 'sh',
    'щ': 'sh',
    'з': 'z',
    'ф': 'f',
    'в': 'v',
    'а': 'a',
    'п': 'p',
    'р': 'r',
    'о': 'o',
    'л': 'l',
    'д': 'd',
    'ч': 'ch',
    'с': 's',
    'м': 'm',
    'и': 'i',
    'т': 't',
    'б': 'b',
    'ж': 'j',
    'е': 'e',
    'э': 'e',
    'х': 'x',
    'ъ': "'",
    'я': 'ya',
    'ю': 'yu',
    'ы': 'i',
    ' ': ' ',
    'ё': 'yo'
     }
lotincha_katta = {
    'Й': 'Y',
    'Ё': 'Yo',
    'Ғ': "G'",
    'Ў': "O'",
    'Қ': 'Q',
    'Ҳ': 'H',
    'У': 'U',
    'К': 'K',
    'Н': 'N',
    'Г': 'G',
    'Ш': 'Sh',
    'Щ': 'Sh',
    'З': 'Z',
    'Ф': 'F',
    'В': 'V',
    'А': 'A',
    'П': 'P',
    'Р': 'R',
    'О': 'O',
    'Л': 'L',
    'Д': 'D',
    'Ч': 'CH',
    'С': 'S',
    'М': 'M',
    'И': 'I',
    'Т': 'T',
    'Б': 'B',
    'Ж': 'J',
    'Е': 'E',
    'Э': 'E',
    'Х': 'X',
    'Ъ': "'",
    'Я': 'Ya',
    'Ю': 'Yu',
    'Ы': 'I',
    ' ': ' '
     }

new_word = ''
for i in range(0,len(word)):
    if word[i] in lotincha.keys() or lotincha_katta.keys():
        if word[i].lower() == word[i]:
            if i == 0 and word[i] == 'ц':
                new_word += 's'
            else:
                if word[i]=='ц':
                        if word[i-1]==' ':
                            new_word += 's'
                        else:
                            new_word+='ts'
                for j in lotincha:

                    if word[i] == j:
                        new_word += lotincha[j]
        else:
            if i == 0 and word[i] == 'Ц':
                new_word += 'S'
            else:
                if word[i]=='Ц':
                        if word[i-1]==' ' or '':
                            new_word += 'S'
                        else:
                            new_word+='TS'
                for j in lotincha_katta:

                    if word[i] == j:
                        new_word += lotincha_katta[j]
    else:
        new_word+=word[i]
print(new_word)