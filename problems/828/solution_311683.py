def primo(num):
    """dado um numero int postivo, a função retorna true ou false se o numero for
    primo ou nao;
    int->bool"""
    d = []
    for i in range(1,num+1):
        if num%i == 0:
            list.append(d,i):
    if len(d)>2:
        return False
    else:
        return True