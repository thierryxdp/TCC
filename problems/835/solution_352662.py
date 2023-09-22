def melhor_volta(matriz):
   '''Função que recebe matriz de voltas com tempos, e 
   verifica quem fez a melhor volta,com que tempo e em
   que volta, e retorna tupla com dados nessa ordem. 
   list --> tuple'''
   list_tempos = []
   list_voltas = []
   for voltas in range(6):
       for tempos in range(10):
           if matriz[voltas][tempos] == min(matriz[voltas]):
               list_tempos.append(tempos)
 
   for i in range(6):
       list_voltas.append(matriz[i][list_tempos[i]])
 
   volta = list_voltas.index(min(list_voltas)
   tempo = min(list_voltas)
   piloto = matriz[volta].index(tempo) + 1
                           
   tupla = (volta + 1, tempo, piloto)
 
   return tupla