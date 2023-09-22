def primo(numero):
    '''Dado um número inteiro positivo, se o número for
    primo retorna True, caso contrário, retorna False.
    int -> bool'''
    lista_divisores=[]
    for i in range(1,numero+1):
        if numero%i==0:
            list.append(lista_divisores,i)
    if len(lista_divisores)==2:
        return True
    else:
        return False