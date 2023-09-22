def primo(n):
    '''Essa função ao receber como valor de entrada um número inteiro e positivo,ela retornara um valor booleanor'''
    '''int -> bool'''
    d= []
    for i in range(1,n+1):
        if n%i == 0:
            list.append (d<i)
    if len(d)== 2:
        return True
    else:
        return False