def maiores(lista,n):
    """ Dada uma lista, retorna outra com numeros maiores de n
list,int--> list"""
    lista.append(n)
    lista.sort()
    posicao= lista.index(n)
    
   
    return lista[posicao +1::]