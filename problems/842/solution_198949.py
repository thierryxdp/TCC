def pontos_por_time(lista):
        '''Esta função retorna um dicionário com o nome de um time e su pontuação.
        list->dict'''
        
        if lista[0][2][0]==lista[0][2][1]:
            pontos1=1
            pontos2=1
        if lista[1][2][0]==lista[1][2][1]:
            pontos1=1+pontos1
            pontos2=1+pontos2
        if lista[0][2][0]>lista[0][2][1]:
            pontos1=3
            pontos2=0
        if lista[0][2][1]>lista[0][2][0]:
            pontos1=+0
            pontos2=+3
        if lista[1][2][0]>lista[1][2][1]:
            pontos1=0+pontos1
            pontos2=3+ pontos2
        if lista[1][2][1]>lista[1][2][0]:
            pontos1=3+pontos1
            pontos2=0+ pontos2
       
        
        return {str(lista[0][1]):pontos2,str(lista[0][0]):pontos1}