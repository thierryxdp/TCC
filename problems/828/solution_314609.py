def primo(numero):
    """funcao que retorna True se um numero é primo e False se nao é primo;
       int->bool"""
    divisores=[]
    for i in range(1,numero+1):
        if numero%i==0:
            divisores=divisores+[i,]
    if divisores[0]==1 and divisores[1]==numero:
        return True
    else:
        return False