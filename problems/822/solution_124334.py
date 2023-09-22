def repetidos(l):
    """Função que retorna o numero de vezes que um elemento é repetido.
    lista -> int."""
    posicao = 1
    repetidos = 0
    while posicao <= len(l)-1:
        if l[posicao] == l[posicao-1]:
            repetidos=repetidos+1
        posicao = posicao+1
    return repetidos