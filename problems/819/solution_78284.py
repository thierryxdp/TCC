def filtraMultiplos(lista,n):
    """função que dada uma lista e um número 'n', retorne uma lista com os valores divisiveis por 'n' da lista original;list,int-->list"""
    x=0
    listaDivisiveis=[]
    while x<len(lista):
        if lista[x]%n==0:
            listaDivisiveis+=[lista[x]]
        x+=1
    return listaDivisiveis