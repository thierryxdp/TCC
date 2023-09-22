def faltante(lista):
    '''recebe uma lista de tamanho n-1 que vai de 1 até n com um número faltando e é retornado o número faltante;lista->int'''
    i=0
    n=len(lista)+2
    l=list(range(1,n))
    while l[i] in lista:
        i+=1
    return l[i]