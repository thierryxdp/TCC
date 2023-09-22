def media matriz(m):
    soma=0
    if len(m)==0:
        return 0.00
    else:
        numeroLinha=len(m)
        numeroColuna=len(m[0])
        for i in range(len(m)):
            soma=soma+sum(m[i])
        return round(soma/(numeroLinha*numeroColuna),2)