def pontos_por_time(jogos):
    '''funcao que recebe uma lista com dois elementos e retorna um dicionario cujos mapeamentos sao nome do time e numero total de pontos.list, list -> list'''
    pontos = {jogos[0][0]:0, jogos[0][1]: 0}
    if jogos[0][2][0]>jogos[0][2][1]:
        pontos[jogos[0][0]]=3
        elif jogos[0][2][0]==jogos[0][2][1]:
            pontos[jogos[0][0]]+=1
            pontos[jogos[0][1]+=1
                   else:
                   pontos[jogos[0][1]]+=3
                   if jogos[1][2][0]>jogos[1][2][1]:
                   pontos[jogos[1][0]]+=3
                   elif jogos[1][2][0]==jogos[1][2][1]:
                   pontos[jogos[1][0]]+=1
                   pontos[jogos[1][2]]+=3
                   else:
                   pontos[jogos[1][1]]+=3
                   return pontos