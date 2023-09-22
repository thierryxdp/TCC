def filtraMultiplos(lista,n):
    '''Função que tendo como entrada uma lista de números e 
    um número retorne uma nova lista com apenas os números
    divisíveis pelo número.'''
    a=0
    resultado=[]
    while a<len(lista):
        if lista[a]%n==0:
            resultado+=[lista[a]]
        a+=1
    return resultado