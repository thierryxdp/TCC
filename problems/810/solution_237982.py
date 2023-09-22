def inverte(frase):
    lista1 = frase.split('-')
    str1 = str.join(' ', lista1)
    lista2 = str1.split(',')
    str2 = str.join(' ', lista2)
    lista3 = str2.split(':')
    str3 = str.join(' ', lista3)
    lista4 = str3.split(';')
    str4 = str.join(' ', lista4)
    lista5 = str4.split('...')
    str5 = str.join(' ', lista5)
    lista6 = str5.split('!')
    str6 = str.join(' ', lista6)
    lista7 = str6.split('?')
    str7 = str.join(' ', lista7)
    lista8 = str7.split('.')
    str8 = str.join(' ', lista8)
    lista9 = str8.split(' ')
    list.reverse(lista9)
    del lista9[0]
    if ('') in lista9:
        del lista9[lista9.index('')]
        del lista9[lista9.index('')]
    str9 = str.join(' ', lista9)
    str10 = str9.lower()
    return str10