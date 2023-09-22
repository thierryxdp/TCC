def posLetra(string,letra,ocorrencia):
    
    i=0
    
    xtotal=''

    """
    str,str,int--->int
    Conforme a posicao da letra na string desejada, se faz sua localizacao
    por meio da funcao index e, relacionando o numero de ocorrencias
    com o tamanho da string pela funcao count,é possivel chegar ao resultado
    
    """
    
    while i<len(string):
        
        if string[i] in letra:
            x=str.index(string,letra)
            return x
        i+=1
        
        if str.count(string,letra)<ocorrencia:

            return -1