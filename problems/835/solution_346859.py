def melhor_volta(matriz):
    
    lista=[]
    
    for corredores in matriz:
        for tempototal in corredores:
            lista+=[tempototal]
     
    tempo_minimo= min(lista)
    corredores=(lista.index(tempo_minimo))//10
    volta=(lista.index(tempo_minimo))%10
    
    return corredores+1,tempo_minimo,volta+1