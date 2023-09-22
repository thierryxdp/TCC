def primo(numero):
    '''Informa se o número de entrada é primo ou não. int->bool.'''
    lista=[]
    for n in range(2,numero+1):
        if (numero%n)==0:
            list.append(lista,n)
    if len(lista)==1:
        return True
    else:
        return False