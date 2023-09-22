def pontos_por_time(lista):
    """recebe uma lista que tem informações do número de gols em dois jogos entre
    dois times e retorna um dicionário que faz a correspondência do time e seu total de 
    pontos na fase.
    lista->dicionario"""
    resultado={'Cormengo':((lista[0])[2])[0]+((lista[1])[2])[1],'Flamínthians':((lista[0])[2])[1]+((lista[1])[2])[0]}
    return resultado