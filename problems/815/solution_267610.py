def insere(lista_numeros,n):
    '''funcao que dado uma lista de numeros ordenados
    e um numero 'n' insere esse numero de modo que
    a lista continua ordenada; list,int -> list'''
    
    inserir = list.insert(lista_numeros,0,n)
    ordenar = list.sort(inserir)
    lista = ordenar
    return lista