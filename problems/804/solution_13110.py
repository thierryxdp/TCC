def filtra_pares(tupla_elementos):
    '''Função que retorna a filtragrem de elementos
    pares de uma tupla. Recebe como parâmetro uma tupla
    de 4 elementos inserida pelo usuário. tupla--> tupla'''#Start your python function here
    if(tupla_elementos[0]%2==0):
        a=tupla_elementos[0]
    else:
        a= ' '
    if(tupla_elementos[1]%2==0):
        b=tupla_elementos[1]
    else:
        b= ' '
    if(tupla_elementos[2]%2==0):
        c=tupla_elementos[2]
    else:
        c= ' '
    if(tupla_elementos[3]%2==0):
        d=tupla_elementos[3]
    else:
        d= ' '

    return (a,b,c,d)