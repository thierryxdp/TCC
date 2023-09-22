def pontos_por_time(nome):
    '''funçao que calcula e retorna um dicionario com o nome do time
    e o numero total de pontos na fase. list-> dict'''
    nome1 = nome[0]
    nome2 = nome[1]
    nome = [nome1 + nome2]
    nome3 = nome1[2]
    nome4 = nome2[2]
    if nome3[0] > nome3[1] and nome4[0] < nome4[1]:
        return {nome[0]:6, nome1[1]:0}
    elif nome3[0] > nome3[1] and nome4[0] > nome4[1]:
        return {nome1[0]:3, nome1[1]:3}
    elif (nome3[0] > nome3[1] and nome4[0] ==nome4[1]) or (nome3[0] == nome3[1] and nome4[0] < nome4[1]):
        return {nome1[0]:4, nome1[1]:1}
    elif nome3[0] < nome3[1] and nome4[0] < nome4[1]:
        return {nome1[0]:3, nome1[1]:3}
    elif nome3[0] < nome3[1] and nome4[0] > nome4[1]:
        return {nome1[0]:0, nome1[1]:6}
    elif (nome3[0] == nome3[1] and nome4[0] >nome4[1]) or (nome3[0] < nome3[1] and nome4[0] == nome4[1]):
        return {nome1[0]:1, nome1[1]:4}
    else:
        return {nome1[0]:2, nome1[1]:2}