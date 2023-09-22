def lingua_p(palavra):
    lista = [char for char in palavra]
    q = 0

    for i in lista[:]:
        q += 1
        if i.lower() in 'aeiou':
            if q != len(lista[:]) -1:
                lista.insert(q, 'p' + str(i))
            else:
                lista.insert(q + 2, 'p' + str(i))

    palavra = str.join('', lista)

    return palavra.casefold()