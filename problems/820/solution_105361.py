def posLetra(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    contador = 0
    posicao = 0
    indice = 0
    if letra not in frase or str.count(frase,letra) < n_ocorrencia:
        return -1
    while contador < n_ocorrencia:
        indice = str.index(frase[indice:],letra)
        contador +=1
    return indice