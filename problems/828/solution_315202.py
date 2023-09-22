def primo (numero):
    '''incluído um número inteiro e positivo'''
    '''int->bool'''
    div= []
    for i in range(1, numero+1):
        if numero%i == 0:
            list.append (div, i)
    if len(div) == 2:
        return True
    else:
        return False