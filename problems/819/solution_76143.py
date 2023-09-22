def filtraMultiplos (numeros,n):
    multiplos=[]
    proximo=0
    while proximo<len(numeros):
        if n%numeros[proximo]==0:
            proximo=proximo+1
            multiplos=multiplos+[numeros[proximo]]
    return multiplos