def posLetra(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    contador = 0
    indice = 0
    if letra not in frase or str.count(frase,letra) < n_ocorrencia or n_ocorrencia == 0:
        return -1
    else:
        if frase[0]==letra and n_ocorrencia>1:
            indice=1
        while contador < n_ocorrencia:
            indice = str.index(frase,letra,indice)
            contador +=1
    return indice

def posLetra2(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    posicao = 0
    parada = n_ocorrencia
    if letra not in frase or str.count(frase,letra) < n_ocorrencia:
        return -1
    else:
        while parada != 0:
            if frase[posicao] == letra:
                parada -= 1
            posicao += 1
    return posicao - 1