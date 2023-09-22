def posLetra(frase, letra, o):
    """essa função recebe uma frase, uma letra e uma ocorrencia e retorna a posição da ocorrencia dada
    entrada: Frase=string; letra= string; ocorrencia(o)= inteiro. Saida: Inteiro"""
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