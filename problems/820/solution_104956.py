def posLetra(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    if letra not in frase:
        return -1
    elif n_ocorrencia > str.find(frase,letra,n_ocorrencia):
        return -1
    return str.index(frase,letra,n_ocorrencia)