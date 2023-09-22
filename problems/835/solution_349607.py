def melhor_volta(mat):
    menor = []
    volta = []
    i = 0
    for linha in mat:
        list.append(menor,min(linha))
        list.append(volta,list.index(linha, menor[i]))
        i += 1   
    menorTem = min(menor)
    menorVol = volta.index(menor.index(menorTem))
    menorCor = menor.index(menorTem)
    return (menorCor, menorTem, menorVol)