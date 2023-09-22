def bolos(a,b,c):
    farinha=a//2
    ovos=b//3
    leite=c//5
    if farinha<leite or farinha<ovos:
        return farinha
    else:
        if ovos<leite or ovos<farinha:
            return ovos
        else:
            return leite