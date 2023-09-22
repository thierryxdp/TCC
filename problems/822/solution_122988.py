def repetidos(lista):
    """Retorna o numero de vezes que um elemento da lista é igual ao 
    elemento anterior, dado: uma lista de numeros."""
    anterior=0
    atual=0
    contador=0
    vezes=0
    
    while contador<len(lista):
        
        if contador==0:
            atual=lista[contador]
        else:
            atual=lista[contador]
        if anterior==atual:
                vezes+=1
        anterior=atual
        contador+=1
    return vezes