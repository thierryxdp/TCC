def lingua_p(palavra):
    lista = []
    palavra = palavra.lower()
    for i in range(0,len(palavra)):
        lista.append(palavra[i])
    for item in range(0, len(lista)):
        if lista[item] in 'aeiou':
            lista[item] = lista[item] + 'p' + lista[item]
    word = ''.join(lista)
    return str(word)