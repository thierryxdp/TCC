def primo(num):
    '''Retorna True se o número inserido for primo e False caso contrário
    ; int -> bool'''
    if num<=1:
        return False
    divisores=0
    anteriores=list(range(num))+[num]
    anteriores.remove(0)
    for i in anteriores:
        if num%i==0:
            divisores=divisores+1
    if divisores>2:
        return False
    else:
        return True