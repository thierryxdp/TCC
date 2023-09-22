def primo(x):
    """essa funcao recebe um numero inteiro positivo e verifica se este numero e positivo ou nao, e retorna um valor booleano; int-> bool""" 
    if x>=2:
        for y in range(2,x):
            if not(x%y):
                return False
             
    else:
        return False
    return True