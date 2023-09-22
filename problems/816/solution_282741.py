def maiores (lis,x):
    """Função que dada uma lista de números inteiros e um número inteiro x, retorna outra lista, que contenha todos os números da lista origina maiores que x, ordenadoos em ordem crescente"""
    """list,int->list"""
    if x in lis:
        list.insert(lis,0,x)
        list.sort(lis)
        y=lis[z+2:]
        z=list.index(lis,x)
        return y
    else:
        list.insert(lis,0,x)
        list.sort(lis)
        y=lis[z+1:]
        z=list.index(lis,x)
        return y