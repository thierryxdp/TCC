def maiores(l,n):
    ''' retorna outra lista que contenha todos os números de l, dada uma lista de números inteiros e um número inteiro n;
    list,int -> list '''
    if n in l:
        list.sort(l)
        l1 = list.index (l,n)
        return l[l1+1:]
    else:
        list.append(l,n) 
        list.sort(l)
        l1 = list.index(l,n)
        return l[l1+1:]