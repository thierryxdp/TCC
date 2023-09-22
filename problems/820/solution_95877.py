def posLetra(frase, letra, o):
    '''recebe uma string, uma letra e um numero que indica uma 
    ocorrência e retorna em que posição a string o numero da ocorrrencia 
    a letra está'''
    fraselist = []
    u = 0
    while u < len(frase):
        fraselist.append(frase[u])
        u=u+1
    i = 0
    indices = []
    while i < len(fraselist):
        if fraselist[i] == letra:
            indices.append(i)
        i=i+1
    if o > len(indices):
        return -1
    else:
        return indices[o-1]