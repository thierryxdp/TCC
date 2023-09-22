def pontos(a):
    if (a[0][2][0]) > (a[0][2][1]):
        return 3
    if (a[0][2][0]) == (a[0][2][1]):
        return 1
    else:
        return 0

def pontos1(b):
    if (b[1][2][1]) > (b[1][2][0]):
        return 3
    if (b[1][2][1]) == (b[1][2][0]):
        return 1
    else:
        return 0


def pontos_por_time(a):
    '''Esta função contabiliza os pontos de dois jogos realizados pelos times, contabilizando o jogo
    de ida e de volta, e retorna o placar de pontos geral.
    assinatura list -> dict
    testes :

    pontos_por_time([['Botameiras','Paulo da gama', [2,2]], ['Paulo da gama','Botameiras',[2,2]]])
     = {'Botameiras': 2, 'Paulo da gama': 2}

     pontos_por_time([['Botameiras','Paulo da gama', [1,0]], ['Paulo da gama','Botameiras',[4,3]]])
     ={'Botameiras': 3, 'Paulo da gama': 3}

     pontos_por_time([['Botameiras','Paulo da gama', [1,5]], ['Paulo da gama','Botameiras',[4,0]]])
     ={'Botameiras': 0, 'Paulo da gama': 6}

     '''
    if pontos(a) + pontos1(a) == 0:
        return {(a[0][0]): pontos(a)+ pontos1(a), (a[0][1]): 6}
    if pontos(a) + pontos1(a) == 1:
        return {(a[0][0]): pontos(a)+ pontos1(a), (a[0][1]): 4}
    if pontos(a) + pontos1(a) == 2:
        return {(a[0][0]): pontos(a)+ pontos1(a), (a[0][1]): 2}
    if pontos(a) + pontos1(a) == 3:
        return {(a[0][0]): pontos(a)+ pontos1(a),(a[0][1]): 3}
    if pontos(a) + pontos1(a) == 4:
        return {(a[0][0]): pontos(a)+ pontos1(a), (a[0][1]): 1}
    if pontos(a) + pontos1(a) == 6:
        return {(a[0][0]): pontos(a) + pontos1(a), (a[0][1]): 0}