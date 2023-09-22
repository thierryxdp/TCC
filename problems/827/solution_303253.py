def qtd_divisores(numero):
    ''' '''
    lista=list(range(1,(numero+1)))
    resultado=[]
    for n in lista:
        if (numero % n) == 0:
            resultado=resultado+[n]
    return len(resultado)