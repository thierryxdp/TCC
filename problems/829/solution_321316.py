def soma_h(n):
    '''funcao retorna a soma de 1/1 até 1/n. int->float'''
    a=1
    lista=[]
    for i in range(1,n+1):
        a=1/i
        lista.append(a)
    return round(sum(lista),2)