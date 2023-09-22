def repetidos(lista):
    '''dado uma lista, retorna o números de vezes que um elemento é igual ao seu antecessor
    lista->int'''
    lista_comparativa=[' ']+lista[:-1]
    zipado=list(zip(lista_comparativa,lista))
    
    cont= [1 for dupla in zipado if dupla[0]==dupla[1]]
    
    return sum(cont)