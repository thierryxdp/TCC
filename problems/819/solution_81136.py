def filtraMultiplos(lista,n):
    '''funcao que recebe como entrada uma lista de numeros
    e um numero n e retorna outra lista de numeros que forem 
    divisíveis por n e estao presente na lista de entrada
    lista, int- > lista'''
    proximo=0
    lista2=[]
    while proximo<len(lista):
        proximo= proximo+1
        if lista[proximo]%n==0:   
            lista2= lista2 + [lista[proximo]]
           
    return lista2