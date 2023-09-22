def maiores(lista,n):
    '''a função retornaoutra lista que contém todos numeros da lista original maiores que n'''
    
    litsa=lista+[n]
    list.sort(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista= lista[:indice]
    list.reverse(nova_lista)
    
    return nova_lista

print(maiores([0,1,5,6,2,3,10];7))