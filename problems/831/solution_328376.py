def lingua_p(palavra):
    """Traduz uma string fornecida atraves do parametro palavra, na lingua do P.
    Adicionando um p antes de todas as vogais.
    palavra --> string
    lista --> lista
    word --> string
    """
    lista = []
    palavra = palavra.lower()
    for i in range(0,len(palavra)):
        lista.append(palavra[i])
    for item in range(0, len(lista)):
        if lista[item] in 'aeiou':
            lista[item] = lista[item] + 'p' + lista[item]
    return print(''.join(lista))