[['cormengo1','flaminthians',[1,0]],['flaminthians','cormengo',[2,2]]]


def pontos_por_time(lista1,lista2):
    vitoria1=3
    vitoria2=3
    empate=1
    somatorio1=vitoria+empate
    somatorio2=vitoria+empate
    desempenho = {lista1[1][0]:somatorio1,lista1[1][1]:somatorio2}
    if lista[0][-1][0]>lista[1][-1][1]:
        return 3
    if lista[0][-1][0]=lista[1][-1][1]:
        return 1
    if lista[0][-1][0]<lista[1][-1][1]:
        return 3
    if lista[1][-1][0]>lista[1][-1][1]:
        return 3
    if lista[1][-1][0]=lista[1][-1][1]:
        return 1
    if lista[1][-1][0]<lista[1][-1][1]:
        return 3
    return desempenho
   
    
    
    
    
    desempenho