def posLetra (string,letra,numero):
    """função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc).
    e retorna em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
    entrada-> str,str,int
    retorna->int"""
    
    qtd_letra=str.count (string,letra)
    taman_str=len (string)
    procura=0
    indice=0
    
    if qtd_letra <numero:
        return -1
    else:
        while procura <numero:
            indice=indice +str.find (string,letra,indice)
            procura= procura+1
            
    return indice