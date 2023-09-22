def filtra_pares(a,b,c,d):
    """Informe uma trupla com 4 números e a função irá retornar os números pares
        number, number, number, number -> string"""
    if(a%2==0):
        varA = a
    else:
        vara1= str(a)
        varA = vara1[:0]
    if(b%2==0):
        varB = b
    else:
        varb1= str(b)
        varB = varb1[ :0]
    if c%2==0:
        varC = c
    else:
        varc1= str(c)
        varC = varc1[ :0]
    if(d%2==0):
        varD = d
    else:
        varD1= str(d)
        varD = varD1[ :0]       
    return varA,varB,varC,varD#Start your python function here