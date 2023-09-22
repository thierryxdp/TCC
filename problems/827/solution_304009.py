def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores de um número n dado como parametro; int->int'''
    lista=list(range(1,n+1))
    l1=[]
    for c in lista:
        if n%c==0:
            list.append(l1,c)
    return len(l1)