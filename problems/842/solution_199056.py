#Questão 2
def pontos_por_time(lista):
    listaA, listaB = lista
    tabela = {listaA[0]:0,listaA[1]:0}
    placar1 = listaA[2]
    placar2 = listaB[2]
    if placar1[0] > placar1[1]:
        if placar2[0] > placar2[1]:
            tabela[str(listaA[0])] = 6
        elif placar2[0] == placar2[1]:
            tabela[str(listaA[0])] = 4
            tabela[str(listaA[1])] = 1
        else:
            tabela[str(listaA[0])] = 3
            tabela[str(listaA[1])] = 3
    elif placar1[0] == placar1[1]:
            if placar2[0] > placar2[1]:
                tabela[str(listaA[0])] = 4
                tabela[str(listaA[1])] = 1
            elif placar2[0] < placar2[1]:
                tabela[str(listaA[0])] = 1
                tabela[str(listaA[1])] = 4 
            else:
                tabela[str(listaA[0])] = 2
                tabela[str(listaA[1])] = 2
    elif placar1[0] < placar1[1]:
        if placar2[0] > placar2[1]:
            tabela[str(listaA[1])] = 3
            tabela['Flamínthians'] = 3
        elif placar2[0] == placar2[1]:
            tabela[str(listaA[0])] = 1
            tabela[str(listaA[1])] = 4
        else:
            tabela['Flamínthians'] = 6
    return tabela