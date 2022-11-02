string = 'акалакосакорука лакарукарака'
tmpl = 'карука'
len_tmpl = len(tmpl)
len_strn = len(string)

Pi = [0] * len_tmpl

# Пройтись по sample и определить префикс и суффикс

j = 0 # Текущий индекс предполагаемого префикса
i = 1 # Текущий индекс проверяемого символа
while i < len_tmpl:
    if tmpl[j] == tmpl[i]:
        Pi[i] = j + 1
        j += 1
        i += 1
    else:                       # Pi[j] != Pi[i]
        if j == 0:
            Pi[i] = 0
            i += 1
        else:                   # j != 0
            j = Pi[j - 1]

print(Pi)

# Сравнить символы в строке с образцом по алгоритму

i = 0 # Индекс символа из строки
j = 0 # Индекс символа из образца

while i < len_strn:
    if string[i] == tmpl[j]:
        i += 1
        j += 1

        if j == len_tmpl:
            print('Соответствие найдено!')
            break

    else:                       # string[i] != tmpl[j]
        if j > 0:
            j = Pi[j-1]
        else:                   # j == 0
            i += 1

if i == len_strn:
    print('Соответствий не обнаружено!')
