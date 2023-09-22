def inverte(frase):
    lista_final = []
    frase_final = ''
    for i in frase:
        lista_final.append(i)
    for i in lista_final:
        if i in '.,:;-!?':
            lista_final[lista_final.index(i)] = ' '
    for i in lista_final:
        frase_final += i
    frase_final = str.split(frase_final, ' ')
    return str.join(' ', frase_final[::-1])