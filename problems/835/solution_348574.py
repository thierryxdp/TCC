def melhor_volta(A):
    '''Retorna a melhor volta de uma corrida (quem foi, qual tempo em que volta) recebendo uma matriz com o tempo de cada jogador em uma respectiva volta. list(list)->tuple. '''
    lista_tempo=[]
    lista_jogador=[]
    for elem in range(len(A)):
        linha=(A[elem])
        tempo=min(linha)
        list.append(lista_tempo,tempo)
        for n in range (len(linha)):
            lista=[]
            if tempo==linha[n]:
                #Caso fossem valores iguais trabalhariamos com a lista
                list.append(lista,n)
                #Mas como possuem valores diferentes
                list.append(lista_jogador,lista[0])
    melhor_tempo=min(lista_tempo)
    i=lista_tempo.index(melhor_tempo)
    melhor_jogador=lista_jogador[i]
    return ((i+1),melhor_tempo,(melhor_jogador+1))