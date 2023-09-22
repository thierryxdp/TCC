def posLetra(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso a ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    contador = 0
    while contador <= len(frase):
        posicao = str.find(frase,letra,contador,n_ocorrencia)
        contador += 1
    posicao = str.find(frase,letra,contador,n_ocorrencia
    return posicao