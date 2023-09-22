def primo(num):
    '''Funcao que retorna True caso um numero de entrada (num) seja
primo e False caso não seja.
Int -> Bool'''
    divisores= []
    for i in range(1,num+1):
        if num%i == 0:
            divisores += [i,]
            
    if divisores == [1, i]:
        return True
    else:
        return False