def repetidos (lista):
    """Função que retorna a quantidade de vezes que um elemento é igual ao anterior;
       list -> int."""
    i=0
    j= []
    while i < len (lista):
        if lista [i] == lista [i-1]:
            j = j + [lista[i]]
        i = i+1
    return len (j)