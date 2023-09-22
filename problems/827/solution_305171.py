def qtd_divisores(numero):
    '''Calcula a quantidade de divisores de um número. int->int.'''
    lista=[]
    for n in range(1,numero+1):
        if (numero%n)==0:
            list.append(lista,n)
    return len(lista)