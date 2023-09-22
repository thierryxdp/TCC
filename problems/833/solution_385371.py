def conta_numero(numero,m):
    x=0
    if len(m)==0:
        return 0
    else:
        numeroLinhas=len(m)
        numeroColunas=len(m[0])
        for i in m:
            if numero in m[i]:
                x=x+m[i].count(numero)
        return x