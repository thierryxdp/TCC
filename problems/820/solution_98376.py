def posLetra(frase,letra,n):
    """Função que dada uma string (frase), uma 'letra' e um número (n) que indica a ocorrência
    desejada da letra, retorna um número inteiro que indica a posição da string aquela ocorrência
    da letra está, caso a ocorrência da letra seja menor do que a pedida retorna '-1'; str, str,
    int -> int """

    posicao = []
    indice = 0

    while indice < len(frase):
        if (frase[indice] == letra):
            list.extend(posicao,[indice])

        indice += 1
        
        if n > len(posicao):
            return -1
        
    return posicao[n-1]