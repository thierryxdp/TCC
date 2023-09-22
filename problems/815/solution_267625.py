def insere(lista_numeros,n):
    '''funcao que dado uma lista de numeros ordenados
    e um numero 'n' insere esse numero de modo que
    a lista continua ordenada; list,int -> list'''
    
    inserir = list.append(lista_numeros,n)
    ordenar = list.sort(lista_numeros)
    
    return lista_numeros