def busca(setor,matriz):
    registro=[]
    
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            registro+=matriz[i]
            list.remove(registro[i],setor)
            
        
    return registro