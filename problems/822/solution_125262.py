def repetidos(lista):
    """função que retorna o número de vezes
    que um elemento é igual ao seu anterior
    list=>int"""
    
    i=0
    cont = 0
    while i < len(lista)-1:
        if lista[i] == lista[i+1]:
            cont=cont+1
        i=i+1
    return cont