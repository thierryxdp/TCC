def pontos_por_time(ls):
    """
    exemplos:
    {"Flaminthias": 1, "Cormengo": 4} == pontos_por_time([["Cormengo", "Flaminthians", [1,0]], ["Flaminthians", "Cormengo", [2,2]]])
    {"A":3, "B":3} == pontos_por_time([['A', 'B', [10, 0]], ['B', 'A', [1,0]]])
    {'B':3, 'A':3} == pontos_por_time([['A', 'B', [10, 0]], ['B', 'A', [1, 0]]])
    """
    ret = {}
    ida = ls[0] #Pacaembu, ['Cormengo', 'Flaminthians', [1,0]]
    vol = ls[1] #Maracanâ, ['Flaminthians", 'Cormengo", [2,2]]
    
    t1 = ida[0]
    t2 = vol[1]
    
    gt1 = ida[3][0]
    gt2 = ida[3][1]
    
    contabilidade(ret, t1,t2,gt1,gt2)
    return ret
def contabilidade(d,t1,t2,gt1,gt2):
    if gt1 < gt2:
        ret [t2] = 3
        ret [t1] = 0
    if gt2 < gt1:
        ret [t2] = 0
        ret [t1] = 3
    if gt1 == gt1:
        ret [t2] = 1
        ret [t1] = 1