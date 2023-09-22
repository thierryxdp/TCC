def acima_da_media(notas_alunos):
    #list -> list
    #Função que recebe uma lista com as notas dos alunos e retorna uma
    #lista ordenada das notas acima da média
    
    lista_media = list()
    media = sum(notas_alunos)/len(notas_alunos)
    for contador in notas_alunos:
        if contador>media:
            lista_media.append(contador)
    lista_media.sort()
    return lista_media