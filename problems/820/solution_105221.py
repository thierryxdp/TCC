def posLetra(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    fim = 0
    while fim <= n_ocorrencia:
        posicao = str.find(frase, letra,n_ocorrencia,fim)
        fim += 1
    return posicao