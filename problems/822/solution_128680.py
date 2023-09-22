def repetidos (lista_de_numeros):
    '''Dado uma lista de números, a função deve retornar
    o número de vezes que um elemento é igual ao elemento
    anterior;
    list->int'''
    
   
    i=1
    n=len(lista_de_numeros)
    quatidade_repetida=0
    q=0
    
    while(i<n):
        if(lista_de_numeros[i] in lista_de_numeros[q]):
            quatidade_repetida=quatidade_repetida+1
        i=i+1
        q=q+1
           
    return (quatidade_repetida)