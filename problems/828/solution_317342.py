def primo(numero):
    '''
    funcao que diz se um numero dado como entrada
    é primo ou não com os booleanos True para sim,
    e False para não
    int->bool
    '''
    primo=0
    for y in range(1,numero+1):
        if numero%y==0:
            primo=primo+1
    if primo!=2:
        return False
    else:
        return True