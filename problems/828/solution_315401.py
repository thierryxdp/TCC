def primo(n):
    """verifica se o número n é primo (true) ou não(false).
    int->bool"""
    total=[]
    for i in range(1,round(n**0.5)+1):
        if n%i==0:
            total=total+[i]
    if len(total)==1:
        return True
    else:
        return False