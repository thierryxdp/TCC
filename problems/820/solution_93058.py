def posLetra(frase,letra,ocorrencia):
    """Dado uma frase, uma letra e um número que representa a ocorrência desejada da letra; a função retorna a posição que represente onde tal ocorrência da letra está;
    str,str,int->int"""
    indice=0
    repeticoes=1
    while repeticoes!=ocorrencia+1:
        posicao=str.index(frase,letra,indice)
        indice=posicao+1
        repeticoes=repeticoes+1
        
    return posicao