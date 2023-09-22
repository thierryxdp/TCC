def posLetra(frase:str,letra:str,ocorrencia:int)->int:
    
    """ Recebe como entrada uma string(frase), uma letra(letra), e um núumero(ocorrencia) que indica a
ocorrência desejada da letra) e retorna em que posição da string aquela ocorrência da letra está. Caso
exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1.

	"""
    
    if str.count(frase,letra)>=ocorrencia:
        
        n = 0
        quantas_vezes = 0
        
        while quantas_vezes <=ocorrencia:
            
            posicao = str.index(frase,letra,n)
            quantas_vezes += 1
            n = posicao + 1
            
        return posicao
    else:
        return -1