def lingua_p(palavra:str) -> str:
    lista = list()
    x = 0
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            lista.append(letra)
            lista.append('p')
            lista.append(letra)
        else:
            list.append(letra)
            
    return str(lista)