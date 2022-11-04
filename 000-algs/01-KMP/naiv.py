strn = 'asetiasaticon drastrasit'
tmpl = 'asito'

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
        if i == l_strn - l_tmpl:
            break

        i += 1
        j = 0

if j == 0:
    print('Такой подстроки нет')
else:
    print('Соответствие найдено')
