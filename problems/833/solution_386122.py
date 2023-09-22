def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    for i in range(nlinhas):
        novalista=[]
        for j in range(mcolunas):
            if numero in nlinhas:
                nlinhas.count(numero)
                n1=nlinhas.count(numero)
            elif numero in mcolunas:
                mcolunas.count(numero)
                n2=mcolunas.count(numero)
                novalista.append(n1,n2)
    return sum(novalista)