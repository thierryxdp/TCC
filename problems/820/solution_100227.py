def posLetra(string,letra,numero):
    """
    Recebe uma string, letra e um numero que indica a ocorrencia
    desejada da letra, e retorna em que posição da string aquela
    ocorrência da letra está. Caso ocorra menos ocorrências do que 
    a pedida da letra, a função retorna -1;
    str,str,int->int
    """    
    i = 0
    if string.count(letra) < numero:
        return -1
    while i < len(string):
    	if string.count(letra) >= numero:
        	texto = string.find(letra,numero*5)
    	i=i+1
    return texto