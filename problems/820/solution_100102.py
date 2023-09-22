def posLetra(string,letra,n):  
    """
    Função que recebe uma frase, uma letra e um número. Com isso, retornamos a posição da 
    frase que aquela ocorrência da letra está.
    str, str, int -> int
    """
    i = 0
    ocorrencia = str.count(string,letra)
    
    while i < len(string):
        if letra in string or n <= ocorrencia:    
        	posicao = str.find(string,letra,ocorrencia)
        else:
            posicao = (-1)
    	i = i + 1
    
    return posicao