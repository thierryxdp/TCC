def faltante(lista):
    """funcao que recebe uma uma lista de numeros, descobre qual numero está faltando e retorna este elemento.
    entrada->list
    saida->int """
    i=0
    list.sort(lista)
    list.append(lista,(len(lista)+1))
    
    while i< len(lista):
        if lista[i]!= i+1:
            return i+1
        i=i+1
    return i