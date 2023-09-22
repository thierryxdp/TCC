def primo(n):
    """ dado um numero inteiro positivo, verifica se o numero e primo ou nao;
    int->bool"""
    x=1
    aux=0
    for i in range(n) :
        if  n%x==0 :
            aux=aux+1
        x=x+1
    if  aux==2:
        return True
    else:
        return False