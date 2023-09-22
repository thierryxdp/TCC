def pontos_por_time(lista):
        '''Esta função retorna um dicionário com o nome de um time e su pontuação.
        list->dict'''
    
        if lista[0][2][0]>lista[0][2][1]:
            pontos_cormengo=3
            pontos_flaminthians=0
        if lista[0][2][1]>lista[0][2][0]:
            pontos_cormengo=0+pontos_cormengo
            pontos_flaminthians=3+pontos_flaminthians
        if lista[1][2][0]>lista[1][2][1]:
            pontos_cormengo=0+pontos_cormengo
            pontos_flaminthians=3+ pontos_flaminthians
        if lista[1][2][1]>lista[1][2][0]:
            pontos_cormengo=3+pontos_cormengo
            pontos_flaminthians=0+ pontos_flaminthians
        if lista[0][2][0]==lista[0][2][1]:
            pontos_cormengo=1+pontos_cormengo
            pontos_flaminthians=1+ pontos_flaminthians
        if lista[1][2][0]==lista[1][2][1]:
            pontos_cormengo=1+pontos_cormengo
            pontos_flaminthians=1+ pontos_flaminthians
        
        return {'flaminthians':pontos_flaminthians,'cormengo':pontos_cormengo}