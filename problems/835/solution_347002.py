def melhor_volta(m):
    lista=[]
    for corredores_pista in m:
        for tempo_percurso in corredores_pista:
            lista+=[tempo_percurso]
            
    menor_tempo=min(lista)
    corredores_pista=(lista.index(menor_tempo))//10
    volta=(lista.index(menor_tempo))%10
    return corredores_pista+1,menor_tempo,volta+1