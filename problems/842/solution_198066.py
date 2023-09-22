def pontos_por_time(pontos):
    if pontos[0][2][0]==pontos[0][2][1] and pontos[1][2][0]==pontos[0][2][1]:
        tabela={pontos[0][0]:2,pontos[0][1]:2}
    elif pontos[0][2][0]==pontos[0][2][1] and pontos[1][2][0]>pontos[1][2][1]:
        tabela={pontos[0][0]:1,pontos[0][1]:4}
    elif pontos[0][2][0]==pontos[0][2][1] and pontos[1][2][0]<pontos[1][2][1]:
        tabela={pontos[0][0]:4,pontos[0][1]:1}
    elif pontos[0][2][0]>pontos[0][2][1] and pontos[1][2][0]==pontos[1][2][1]:
        tabela={pontos[0][0]:4,pontos[0][1]:1}
    elif pontos[0][2][0]>pontos[0][2][1] and pontos[1][2][0]<pontos[1][2][1]:
        tabela={pontos[0][0]:6,pontos[0][1]:0}
    elif pontos[0][2][0]>pontos[0][2][1] and pontos[1][2][0]>pontos[1][2][1]:
        tabela={pontos[0][0]:3,pontos[0][1]:3}
    elif pontos[0][2][0]<pontos[0][2][1] and pontos[1][2][0]==pontos[1][2][1]:
        tabela={pontos[0][0]:1,pontos[0][1]:4}
    elif pontos[0][2][0]<pontos[0][2][1] and pontos[1][2][0]<pontos[1][2][1]:
        tabela={pontos[0][0]:3,pontos[0][1]:3}
    elif pontos[0][2][0]<pontos[0][2][1] and pontos[1][2][0]>pontos[1][2][1]:
        tabela={pontos[0][0]:0,pontos[0][1]:6}
        return tabela