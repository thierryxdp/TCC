def filtraMultiplos(lista,n):
    '''funcao que recebe como entrada uma lista de numeros
    e um numero n e retorna outra lista de numeros que forem 
    divisíveis por n e estao presente na lista de entrada
    lista, int- > lista'''
    proximo=0
    lista2=[]
    while lista[proximo]==1:
        lista2= lista2 + [lista[proximo]]
        proximo= proximo+1
        return lista2