def posLetra(string,letra,n):
    """funçao que recebe como entrada uma string, uma letra e um numero que indica a ocorrencia desejada da letra, e a função retorna a posição que a ocorrencia daquela letra está"""
    indice=0
    posicao=[]
    if str.count(string, letra)<n:
        return -1
    while indice<len(string):
        if string[indice]==letra:
            list.append(posicao,indice)
        indice= indice+1
    return posicao[n-1]