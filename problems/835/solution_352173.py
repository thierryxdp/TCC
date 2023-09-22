def melhor_volta(matriz):
    '''
    	Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e
        retorna uma tupla informando quem foi a melhor volta da prova, com qual tempo e em que volta.
        list -> tuple
    '''
    menores_voltas = []
    dicio = {}
    for i in range(0,len(matriz)): #Cria um dicionário que corresponde o corredor com seu melhor tempo.
        dicio.update({i+1:min(matriz[i])})
        
    menor_tempo = min(dicio.values()) #Encontra o menor tempo feito dentro do dicionario.
    
    #Com o valor de menor tempo, devemos achar a chave, ou seja, o corredor.
    listadechaves = list(dicio.keys())
    listadevalores = list(dicio.values())
    position = listadevalores.index(menor_tempo)
    corredor = listadechaves[position]
    
    #Encontra qual foi a volta que fez o menor tempo
    numero_da_volta = matriz[corredor-1].index(menor_tempo) + 1
    
    return (corredor,menor_tempo, numero_da_volta)