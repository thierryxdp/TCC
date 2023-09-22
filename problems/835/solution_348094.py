def melhor_volta(matriz):
    '''retorna uma tupla com o corredor que teve o menor tempo,
    o menor tempo da corrida, e em qual volta foi feito
    list(list) -> tuple'''
    
    listam = []
    
    for i in range(6):
        mini = min(matriz[i])
        listam += [mini]
        
    menordetodos = min(listam)
    
    imenor = list.index(listam,menordetodos)
    imenor_1 = list.index(listam,menordetodos) + 1
    
    menorvolta = list.index(matriz[imenor],menordetodos) + 1
    
    return (imenor_1,menordetodos,menorvolta)