def melhor_volta(matriz):
    
    lista=[]
    
    for corredor in matriz:
        for tempo_todos in corredor:
            lista+=[tempo_todos]
     
    menor_tempo= min(lista)
    corredor=(lista.index(menor_tempo))//10
    volta=matriz[(lista.index(menor_tempo))%10]
    
    return corredor+1,menor_tempo,volta