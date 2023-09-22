def filtraMultiplos(lista_de_numeros,numero):
    '''Dado uma lista de números e um número, a função deve
    retornar outra lista só com os números da lista original
    que são divisíveis pelo número dado;
    list, int ->list'''
    
    i=0
    lista_de_divisores=[]
    n=len(lista_de_numeros)
    while (i<n):
        if((lista_de_numeros[i])%numero==0):
            list.append(lista_de_divisores,lista_de_numeros[i])
        i=i+1
        
    return (lista_de_divisores)