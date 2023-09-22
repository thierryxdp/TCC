def posLetra(frase,letra,n):
    """Função que dada uma string (frase), uma 'letra' e um número (n) que indica a ocorrência
    desejada da letra, retorna um número inteiro que indica a posição da string aquela ocorrência
    da letra está, caso a ocorrência da letra seja menor do que a pedida retorna '-1'; str, str,
    int -> int """

    pos = []
    num_elementos = len(frase)
    indice = 0

    while indice < num_elementos:
        if (frase[indice] == letra):
            list.extend(pos,[indice])
        indice += 1

    if n > len(frase):
        return -1
    return pos[n-1]