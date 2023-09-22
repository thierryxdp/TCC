def melhor_volta(matriz):
     """Dada uma matriz contendo o tempo em segundos
     de 6 corredores ao longo das 10 voltas em uma pista
     de Kart, a função retorna uma tupla contendo de quem
     foi a melhores volta, qual foi o tempo e em que volta
     isso ocorreu.
     Parametros de Entrada: list
     Retorna: tupla"""

     tempo= []
     volta=1
     corredor=1

     for i in range(len(matriz)):
         list.append(tempo,min(matriz[i]) 
     tempo=min(tempo)

     for i in range(len(matriz)):
         for j in range(len(matriz[i])):
             if tempo == matriz[i][j]:
                 volta=volta+j
                 corredor=corredor+i
         
     return tuple([corredor,volta,tempo])