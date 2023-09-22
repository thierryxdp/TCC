def lingua_p(palavra:str) -> str:
    lista = list()
    x = 0
    for letra in palavra:
        if letra.lower() not in 'bcdfghjklmnpqrstvwxyz':
            lista.append(letra)
            lista.append('p')
            lista.append(letra)
        else:
            lista.append(letra)
            
    return str.join("",lista).lower()