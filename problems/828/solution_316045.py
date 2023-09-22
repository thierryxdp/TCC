def primo(n):
    '''verifica se um numero inteiro n é primo ou não, retornando
    True caso seja primo e False caso não seja;
    int->bool'''
    divisores=0
    for x in range(2,n):
        if n%x==0:
            divisores+=1
    if divisores>0:
        return False
    else:
        return True