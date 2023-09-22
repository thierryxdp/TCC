def pontos_por_time (lista1):
    '''recebe uma lista com dois elementos, sendo eles duas listas, contendo o número de gols em duas partidas'''
    listafinal = [pontos]
    v= vitoria
    e= empate
    pontos= 3*v+1*e
    for i in range (0,len (lista1)):
        listafinal.append (lista1[i])
        return listafinal