def primo(n):
    '''funcao que, dado um numero inteiro positivo, verifica se ele e ou nao primo,
    retornando True ou False, respectivamente;
    int->bool'''
    qtd=0
    for i in range (1,n+1):
        if (n%i)==0:
            qtd = qtd + 1
    if qtd==2:
        return True
    else:
        return False