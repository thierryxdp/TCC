def maiores(lista,n):
    ''' a função que retorna outra lista que contém todos os numeros da lista original maior que n'''
    lista=lista+ [n]
    list.sort(lista)
    list.reverse(lista)
    
    indice=list.index(lista,n)
    nova_lista= lista[:indice]
    
    list.reserve(nova_lista)
    return