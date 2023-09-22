def pontos_por_time(*jogo):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'list-->(list,list) --> dict'

    jogo=list(jogo)
    jogo_ida=jogo[0] or jogo[4]

    return jogo_ida