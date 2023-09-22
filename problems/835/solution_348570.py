def melhor_volta(A):
    ''''''
    lista_tempo=[]
    lista_jogador=[]
    for elem in range(len(A)):
        linha=(A[elem])
        tempo=min(linha)
        list.append(lista_tempo,tempo)
        for n in range (linha):
            lista=[]
            if tempo==linha[n]:
                #Caso fossem valores iguais trabalhariamos com a lista
                list.append(lista,n)
                #Mas como possuem valores diferentes
                list.append(lista_jogador,lista[0])
    melhor_tempo=min(lista_tempo)
    i=lista_tempo.index(melhor_tempo)
    melhor_jogador=lista_jogador[i]
    return(melhor_jogador,melhor_tempo)