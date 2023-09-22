def posLetra (string,letra,n):
    """retorna em que posição da string aquela ocorrência da letra está, caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1"""
    posicao=-1
    if letra not in string or n>str.count(letra):
        return posicao
    else:
        while n!=0:
            n=n-1
            posicao=str.find(string,letra,posicao+1)
    return posicao