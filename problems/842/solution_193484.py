def pontos_por_time (lista1):
    '''recebe uma lista com dois elementos, sendo eles duas listas, contendo o número de gols em duas partidas'''
    v= vitoria
    e= empate
    pontos= 3*v+1*e
    listafinal = [pontos]
    for i in range (0,len (lista1)):
        listafinal.append (lista1[i])
        return listafinal