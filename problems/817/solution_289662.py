def maiores(a,b):
    '''Dada uma lista de números inteiros(a) e
    um número inteiro(b), retorna outra lista que
    contém todos os números da lista original maiores
    que (b).
    list --> list'''
    x=a[:]
    list.append(x,b)
    list.sort(x)
    y = list.index(x,b)
    return x[y+1:]



def acima_da_media(a):
    '''Dada uma lista com as notas dos alunos, retorna
    uma lista ordenada com as notas acima da média.
    list --> list''' 
   x = len(a)
    y = sum(a)
    z = y/x
    if z in a:
        u = a[:]
        list.sort(u)
        r = list.index(u,z)
        return u[r+1:]
    else:
        return maiores(a,z)