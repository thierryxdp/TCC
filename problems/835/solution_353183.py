def melhor_volta (todos):
    
    a = len(todos)
    vencedor = 0
    tempo = 0
    volta = 0
    lista = []

    for i in range (a):
        for j in range(len(todos[i])):
            lista += [todos[i][j]]
        tempo = min(lista)

        vencedor = 0
        for i in range(a):
            tempos_corredor = todos[i]
            if tempo in tempos_corredor:
                vendedor = i

        volta = list.index(todos[vencedor], tempo)

        return vencedor+1, tempo, volta+1