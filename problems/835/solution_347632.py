def melhor_volta(m):
    """recebe uma matriz com o tempo em segundos dos corredores e retorna de quem foi a melhor volta e qual foi o tempo de volta.
    list->tuple"""
    minimos=[]
    for i in range(len(m)):
        minimos=minimos+[min(m[i]),]
    mintot=min(minimos)
    return (list.index(minimos,mintot)+1,mintot,list.index(m[list.index(minimos,mintot)],mintot)+1)