def primo(n):
    """funcao que dado um numero inteiro n, verifica se n é primo ou não.
    int-->bool"""
    
    numeros=[]
    for a in range (1,n+1):
        if n%a==0:
            list.append(numeros,a)
            a=a+1
            
    if len (numeros)==1:
        return True
    else:
        return False