def qtd_divisores (numero):
    ''' '''
    ''' '''
    div= []
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append (div,i)
    return len(div)