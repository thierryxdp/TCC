def soma_h(n:int)->float:
    """calcula e retornar o valor  H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n com N termos, onde N  ́e inteiro e édado como entrada"""
    soma=0
    for i in range(1,n+1):
        x=round(1/i,2)
        soma+=x
    return soma