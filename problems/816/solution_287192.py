def maiores(l,n):
    ''' retorna outra lista que contenha todos os números de l, dada uma lista de números inteiros e um número inteiro n;
    list,int -> list '''
    if n in l:
        list.sort(l)
        x = list.index (l,n)
        return l[x+1:]
    else:
        list.append(l,n) 
        list.sort(l)
        x = list.index(l,n)
        return l[x+1:]