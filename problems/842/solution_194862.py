def pontos_por_time(lista):
    '''retorna um dicionario cujos mapeamentos sao o nome e o numero de pontos na fase'''
    
    nome1 = lista[0][0]
    nome2 = lista[0][1]
    
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        return {nome1:6, nome2:0}
    
    if lista[0][2][0] < lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        return {nome2:6, nome1:0}
    
    if lista[0][2][0] == lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {nome1:2, nome2:2}
    
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        return {nome1:3, nome2:3}
    
    if lista[0][2][0] < lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        return {nome1:3, nome2:3}
    
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {nome1:4, nome2:1}
    
    if lista[0][2][0] == lista[0][2][1] and lista[1][2][0] < lista[1][2][1]:
        return {nome2:4, nome1:1}