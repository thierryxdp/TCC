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
    if string.count(letra) == 1:
        return string.find(letra)
    while i < len(string):
        		texto = string.find(letra,letra[i])
    		i=i+1
    return texto