def posLetra(frase,letra,n_ocorrencia):
    """def que ao dar de entrada uma frase, uma letra e o numero da ocorrencia dessa letra na frase, retorna a posicao da letra. caso ela nao estiver contida na frase, retorna -1. str,str,int -> int"""
    posicao = 0
    while posicao < len(frase):
    	posicao += str.find(frase,letra,contador,n_ocorrencia)       
    	if posicao >= len(frase)
     		return -1
    	posicao += 1  
    return posicao