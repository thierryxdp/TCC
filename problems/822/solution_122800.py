def repetidos (lista):
    """Funcao que retorna o numero de vezes que um elemento da lista de numeros e igual ao elemento anterior;
    Entrada: list[int]
    Saida: int"""
    
    indice=1
    listao=[]
    
    while indice<len(lista):
        if lista[indice] == lista[indice-1]:
            list.append(listao,1)
        indice = indice +1
    return len(listao)