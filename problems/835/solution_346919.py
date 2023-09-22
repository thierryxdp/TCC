def melhor_volta(voltas):
    tempos = []
    
    for corredores in voltas:
        for tempos in corredores:
            lista_tempos+=[tempos]
            
    melhor_tempo=min(lista_tempos)
    corredor=(lista_tempos.index(melhor_tempo))//10
    volta=(lista_tempos.index(melhor_tempo))%10
    
    return corredor+1, melhor_tempo, volta+1