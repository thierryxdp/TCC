def uppCons(frase):
    """Função que transforma todas as consoantes para maiúsculo.
       Onde "frase" - é o texto que será alterado.
    str --> str """
    lista = []
    for i in frase:
        if i not in 'aeiouãõáéíóúâêîôû':
            lista.append(i.upper())
        else:
            lista.append(i)
    frase_alterada = ''.join(lista)
    return frase_alterada