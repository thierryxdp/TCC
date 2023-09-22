def inverte(frase):
    lista_final = []
    frase_final = ''
    for i in frase:
        lista_final.append(i.lower())
    for i in lista_final:
        if i in ':;.,-!? ':
            lista_final[lista_final.index(i)] = ' '
    lista_final = str.split(str.join('', lista_final), ' ')
    if str.join(' ', lista_final[::-1])[0] == ' ':
        return str.join(' ', lista_final[::-1])[1:]
    else:
        return str.join(' ', lista_final[::-1])