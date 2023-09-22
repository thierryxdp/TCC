def repetidos(lista):
    """
    recebe uma lista e retorna o número de vezes que um número numa 
    posição qualquer i é igual ao número na posição i-1
    """
    
    i=1
    repet=0
    
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repet=repet+1
        i=i+1
    return repet