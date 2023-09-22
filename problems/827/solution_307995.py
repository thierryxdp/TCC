def qtd_divisores(n):
    '''função que conta a quantidade de divisores que um 
    número possui. int->int'''
    lista=[]
    for i in list(range(1,n+1)):
        if n%i==0:
            lista.append(i)
    return len(lista)