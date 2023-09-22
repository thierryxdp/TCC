def primo(n):
    """dado um número inteiro positivo "n", verifica se ele é primo ou não, retornando False caso não seja primo e True caso seja primo;int->bool"""
    if n==1 or n%2==0:
        return False
    num=0
    for val in range(3,n,2):
        if n%val==0:
            num=num+1
    if num>0:
        return False
    else:
        return True