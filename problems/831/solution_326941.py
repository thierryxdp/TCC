def lingua_p(palavra):
    '''Recebe como parâmetro uma palavra (em português) e retorna esta mesma 
    palavra traduzida para a língua do P '''
    palavra = palavra.lower()
    lista = [] 
    for letra in palavra:
        lista.append(letra)
        if letra in 'aeiou':
            list.append(lista, 'p')
            list.append(lista, letra)
    retorno = ''.join(lista)
    return retorno