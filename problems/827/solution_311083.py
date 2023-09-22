def qtd_divisores(numero):
    multiplos=0
    for elemento in range(1,numero):
        if numero % elemento==0:
            multiplos+=1
    if numero<=0:
            return multiplos
    else:
        return multiplos+1