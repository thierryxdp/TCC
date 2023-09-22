def melhor_volta (todos):     
    tempo = todos[0][0]
    a = len(todos)
    vencedor = 0
    lista = []  
    for i in range(a):       
    tempo_corredor = min(todos[i])      
        if tempo_corredor < tempo:          
            tempo = tempo_corredor
            vencedor = i          
    volta = list.index(todos[vencedor], tempo)

    return vencedor+1, tempo, volta+1