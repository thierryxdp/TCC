def soma_h(N):
    """Essa função calcula o valor H dado um número N. Como entrada
    temos N um número inteiro e como saída temos a soma deles;
    int->float"""
    somah=1
    listaN=[]
    for i in range(1,N+1):
        listaN.append(i)
    for valor in listaN:
        dividi=round(1/listaN[i-1],2)
    somah=somah+dividi
    return somah