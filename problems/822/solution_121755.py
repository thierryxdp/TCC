def repetidos (lista):
    """Função que, dada uma lista, retona o número de vezes que um elemento da lista é igual
    ao elemento anterior.
    Entrada: lista[int]
    Saída: int."""
    
    list.sort(lista)
    i=0
    num = []
    
    while i < len(lista):
        if lista[i] == lista[i-1]:
        	list.append(num, lista[i])
        i = i+1
    return num