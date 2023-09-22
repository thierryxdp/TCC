def melhor_volta(m:list)->tuple:
    acumulador=[]
    for i in range(6):
        acumulador.append(min(m[i]))