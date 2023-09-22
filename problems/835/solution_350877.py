def melhor_volta(matriz:list):->tuple:
        '''Função que retorna de quem foi a melhor volta,
        com qual tempo e em que volta'''
        melhor_volta = 0
        tempo = 10000
        corredor = 0
        indice = 1
        
        for i in matriz:
            if min(i) < tempo:
                tempo = min(i)
                corredor = indice
                melhor_volta = i.index(tempo) + 1
            indice += 1
        return (corredor, tempo, melhor_volta)