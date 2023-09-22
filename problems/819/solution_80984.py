filtraMultiplos(lista,n):
    '''funcao que recebe como entrada uma lista de numeros
    e um numero n e retorna outra lista de numeros que forem 
    divisíveis por n e estao presente na lista de entrada
    lista, in- > lista'''
    proximo=0
    lista2=[]
    while lista[proximo]%n!=0:
        lista2= lista2+ lista[proximo]
        return lista2