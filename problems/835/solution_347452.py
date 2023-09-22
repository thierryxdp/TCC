def melhor_volta(tabela_voltas):
    """Recebe uma tabela 6x10 com os tempos em segundos de 10 voltas para cada um dos
       6 corredores e retorna uma tupla contendo o corredor que conseguiu a melhor tempo
       e qual o tempo da melhor volta e qual foi essa volta.
       list->tuple

       Parameters:
       tabela_voltas: Uma tabela 6x10 com os tempos em segundos de 10 voltas para cada um dos
       6 corredores."""
    t=[]
    for linha in tabela_voltas:
        for tempo in linha:
            list.append(t,tempo)

    if list.index(t,min(t))< 10:
        return (1,min(t),list.index(t,min(t))+1)
    elif list.index(t,min(t))<20:
        return (2,min(t),list.index(t,min(t))-9)
    elif list.index(t,min(t))<30:
        return (3,min(t),list.index(t,min(t))-19)
    elif list.index(t,min(t))<40:
        return (4,min(t),list.index(t,min(t))-29)
    elif list.index(t,min(t))<50:
        return (5,min(t),list.index(t,min(t))-39)
    else:
        return (6,min(t),list.index(t,min(t))-49)