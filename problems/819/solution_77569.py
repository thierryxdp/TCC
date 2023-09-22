def filtraMultiplos(lista_num,n):
    '''função que recebe uma lista de números (lista_num) e 
    um número n e retorna uma lista contendo todos os elementos
    da lista original que são multiplos de n;
    list,int-->list'''
    nova_lista=[]
    proximo=0
    while lista_num[proximo]<len(lista_num):
        if lista_num[proximo]%n=0:
            nova_lista=nova_lista+lista_num[proximo]
        proximo=proximo+1
    return nova_lista