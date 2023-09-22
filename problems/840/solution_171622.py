bolos(a,b,c):
    farinha=A//2
    ovos=B//3
    leite=C//5
    if farinha<leite or farinha<ovos:
        return farinha
    else:
        if ovos<leite or ovos<farinha:
            return ovos
        else:
            return leite