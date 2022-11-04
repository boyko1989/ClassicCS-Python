strn = 'asetiasaticon drastrasit'
tmpl = 'asit'

l_tmpl = len(tmpl)
l_strn = len(strn)

print(l_tmpl, l_strn)

i = 0
j = 0

while i < l_strn - 1:
    if strn[i] == tmpl[j]:
        i += 1
        j += 1
    else:  # strn[i] != tmpl[j]
        i += 1
        j = 0

if i == l_strn - 1 and j == l_tmpl - 1:
    print('Соответствие найдено')
else:
    print('Такой подстроки нет')
