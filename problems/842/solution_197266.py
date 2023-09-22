#Start your python function here
def pontos_por_time(x):
    """
    Calcula e retorna um dicionario com os times e os numeros de pontos
    a partir de uma lista com 2 elementos com as informacoes dos jogos;
    list -> dict
    """
    #Cormengo e Cormengo
    if x[0][0] == x[1][0] and x[0][2][0] > x[0][2][1] and x[1][2][0] > x[1][2][1]:
        return {(x[0][0]):6,x[0][1]:0}
    
    elif x[0][0] == x[1][0] and x[0][2][0] > x[0][2][1] and x[1][2][0] < x[1][2][1]:
        return {(x[0][0]):3,x[0][1]:3}
    
    elif x[0][0] == x[1][0] and x[0][2][0] > x[0][2][1] and x[1][2][0] < x[1][2][1]:
        return {(x[0][0]):3,x[0][1]:3}
    
    elif x[0][0] == x[1][0] and x[0][2][0] < x[0][2][1] and x[1][2][0] < x[1][2][1]:
        return {(x[0][0]):0,x[0][1]:6}
    
    
    
    
    #Empates
    elif x[0][2][0] > x[0][2][1] and x[1][2][0] == x[1][2][1]:
        return {(x[0][0]):4,x[0][1]:1}
    
    elif x[0][2][0] == x[0][2][1] and x[1][2][0] > x[1][2][1]:
        return {(x[1][0]):4,x[1][1]:1}
    
    elif x[0][2][0] < x[0][2][1] and x[1][2][0] == x[1][2][1]:
        return {(x[0][0]):1,x[0][1]:4}
    
    elif x[0][2][0] == x[0][2][1] and x[1][2][0] < x[1][2][1]:
        return {(x[1][0]):1,x[1][1]:4}
    
    elif x[0][2][0] == x[0][2][1] and x[1][2][0] == x[1][2][1]:
        return {(x[0][0]):2,x[0][1]:2}
    
    else:
        return "Problema"