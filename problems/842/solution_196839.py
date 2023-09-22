def pontos_por_time(l1):
    """funçao que dada uma lista retorna um dicionario com o nome dos 
    times e o numero de pontos em fase; list->dicionaario"""
    if l1[0][2][0]>l1[0][2][1] and l1[1][2][1]>l1[1][2][0]:
        return {l1[0][0]:6,l1[0][1]:0}
    elif l1[0][2][1]>l1[0][2][0] and l1[1][2][0]>l1[1][2][1]:
        return {l1[0][1]:6,l1[0][0]:0}
    elif l1[0][2][0]>l1[0][2][1] and l1[1][2][1]<l1[1][2][0]:
        return {l1[0][0]:3,l1[0][1]:3}
    elif l1[0][2][0]<l1[0][2][1] and l1[1][2][1]>l1[1][2][0]:
        return {l1[0][0]:3,l1[0][1]:3}
    elif l1[0][2][0]>l1[0][2][1] and l1[1][2][1]==l1[1][2][0]:
        return {l1[0][1]:1,l1[0][0]:4}
    elif l1[0][2][0]<l1[0][2][1] and l1[1][2][1]==l1[1][2][0]:
        return {l1[0][1]:4,l1[0][0]:1}
    elif l1[0][2][0]==l1[0][2][1] and l1[1][2][1]>l1[1][2][0]:
        return {l1[0][1]:1,l1[0][0]:4}
    elif l1[0][2][0]==l1[0][2][1] and l1[1][2][1]<l1[1][2][0]:
        return {l1[0][1]:4,l1[0][0]:1}
    else:
        return {l1[0][1]:2,l1[0][0]:2}