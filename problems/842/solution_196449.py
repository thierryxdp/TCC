def pontos_por_time(lista):
    """recebe uma lista que tem informações do número de gols em dois jogos entre
    dois times e retorna um dicionário que faz a correspondência do time e seu total de 
    pontos na fase.
    lista->dicionario"""
    if ((lista[0])[2])[0]==((lista[0])[2])[1] and ((lista[1])[2])[0]==((lista[1])[2])[1]:
        return {(lista[0])[1]:1+1,(lista[0])[0]:1+1}
    elif ((lista[0])[2])[0]==((lista[0])[2])[1] and ((lista[1])[2])[0]>((lista[1])[2])[1]:
        return {(lista[0])[1]:1+3,(lista[0])[0]:1}
    elif ((lista[0])[2])[0]>((lista[0])[2])[1] and ((lista[1])[2])[0]==((lista[1])[2])[1]:
        return {(lista[0])[1]:1,(lista[0])[0]:3+1}
    elif (((lista[0])[2])[0]>((lista[0])[2])[1] and ((lista[1])[2])[0]>((lista[1])[2])[1]) or (((lista[0])[2])[0]<((lista[0])[2])[1] and ((lista[1])[2])[0]<((lista[1])[2])[1]):
        return {(lista[0])[1]:3,(lista[0])[0]:3}
    elif ((lista[0])[2])[0]<((lista[0])[2])[1] and ((lista[1])[2])[0]>((lista[1])[2])[1]:
        return {(lista[0])[1]:3+3,(lista[0])[0]:0}
    elif ((lista[0])[2])[0]>((lista[0])[2])[1] and ((lista[1])[2])[0]<((lista[1])[2])[1]:
        return {(lista[0])[1]:0,(lista[0])[0]:3+3}