def lingua_p(frase):
    """Recebe uma frase e transforma na lingua dos p.
    str -> str"""
    lista = list(frase)
    cont = 0

    for i in range(0, len(frase)):
        if frase[i] in 'aeiou':
            lista.insert(i + cont, f'p{frase[i]}')
            cont += 2
    juntos = ''.join(lista)
    return juntos