# Dada uma lista de números, esta função retorna o número de vezes que um
# elemento da lisat é igual ao seu anterior nesta mesma lista.
# list -> int
def repetidos(lista):
    lista2 = list.copy(lista)
    lista2.append(0)
    lista2.pop(0)
    
    cont = tuple(zip(lista,lista2))
    
    resp = [1 for elem in cont if elem[0] == elem[1]]
    
    resp = len(resp)
    

    return cont