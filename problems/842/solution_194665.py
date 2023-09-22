def pontos_por_time(time1,time2,n1,n2,n3,n4):
    """essa função recebe o resultado de dois jogos de futebol entre dois times e retorna um mapeamento indicando o numero de pontos de cada time"""
    """entrada: list"""
    """saida: dicionario"""
    if n1==n2 and n3==n4:
        return {time1:2 , time2:2}
    elif n1>>n2 and n3==n4:
        return {time1:4 , time2:1}
    elif n1<<n2 and n3==n4:
        return {time1:1 , time2:4}
    elif n1==n2 and n3>>n4:
        return {time1:1 , time2:4}
    elif n1==n2 and n3<<n4:
        return {time1:4 , time2:1}
    elif n1>>n2 and n3>>n4:
        return {time1:3 , time2:3}
    elif n1<<n2 and n3<<n4:
        return {time1:3 , time2:3}
    elif n1>>n2 and n3<<n4:
        return {time1:6 , time2:0}
    elif n1<<n2 and n3>>n4:
        return {time1:0 , time2:6}