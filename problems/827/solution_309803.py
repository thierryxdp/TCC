def qnt(n):
    """Função que calcula a quantidade de divisores naturais
    de um número n.
    int --> int """
    div=0
    for i in range(1,1000):
        if(n%i==0):
            div+=1
    return div