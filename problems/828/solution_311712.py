def primo(n):
    """Funcao que dado um numero positivo verifica se este é primo ou não;int->bool"""
    lista=list(range(1,n+1))
    vazio=[]
    for i in lista:
        if n%i==0:
            vazio=vazio+[i,]
        else:
            vazio=vazio
    if n==1 or vazio==[1,n]:
        return True
    else:
        return False