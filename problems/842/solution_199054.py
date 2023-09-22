def pontos_por_time(lista):
    listaA, listaB = lista
    tabela = {'Cormengo':0,'flamínthias':0}
    if listaA[0] > listaA[1]:
        if listaB[0] > listaB[1]:
            tabela['Cormengo'] = 6
        elif listaB[0] == listaB[1]:
            tabela['Cormengo'] = 4
            tabela['Flamínthians'] = 1
        else:
            tabela['Cormengo'] = 3
            tabela['Flamínthians'] = 3
    elif listaA[0] == listaA[1]:
            if listaB[0] > listaB[1]:
            tabela['Cormengo'] = 4
            tabela['Flamínthians'] = 1
        elif listaB[0] < listaB[1]:
            tabela['Cormengo'] = 1
            tabela['Flamínthians'] = 4 
        else:
            tabela['Cormengo'] = 2
            tabela['Flamínthians'] = 2
    else:
        if listaB[0] > listaB[1]:
            tabela['Cormengo'] = 3
            tabela['Flamínthians'] = 3
        elif listaB[0] == listaB[1]:
            tabela['Cormengo'] = 1
            tabela['Flamínthians'] = 4
        else:
            tabela['Flamínthians'] = 6
    return tabela