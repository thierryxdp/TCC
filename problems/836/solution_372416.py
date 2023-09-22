def busca (setor, matriz):
    x = 0
    listacont = []
    while x < len(matriz):
        for i in matriz[x]:
            if setor == matriz [x][2]:
                matriz[x].pop(2)
                contato = matriz[x]
                listacont.append(contato)
    return listacont