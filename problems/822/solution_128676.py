def repetidos (lista_de_numeros):
    '''Dado uma lista de números, a função deve retornar
    o número de vezes que um elemento é igual ao elemento
    anterior;
    list->int'''
    
    list.sort(lista_de_numeros)
    i=0
    n=len(lista_de_numeros)
    lista=[]
    
    while(i<n):
        if(lista_de_numeros[i] not in lista):
            if (list.count(lista_de_numeros[i],lista_de_numeros)>1):
                lista = lista + lista_de_numeros[i]
        i= i+1
           
    return (len(lista))