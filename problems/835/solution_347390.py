def melhor_volta(m:list)->tuple:
    acumulador=[]
    for i in range(6):
        acumulador.append(min(m[i]))
    tempo=min(acumulador)
    quem=m.index(min(acumulador))
    return (quem,tempo)