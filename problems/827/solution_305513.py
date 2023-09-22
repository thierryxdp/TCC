def qtd_divisores(n):
    '''funcao retorna a quantidade de divisores de n'''
    lista=[]
    for i in range(1,n+1):
        if n%i==0:
            lista.append(i)
    return len(lista)