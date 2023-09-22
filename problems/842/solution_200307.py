def pontos_por_time(lista1, lista2):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'dict(list,list) --> dict'
    lista1=(lista1[0],lista1[1],lista1[2])
    lista2=(lista2[0],lista2[1],lista2[2])
    vitoria = 3
    empate = 1
    derrota = 0
    
    
    #retornar um dicionario com nome_do_time e numero_de_pontos
    if lista1[2][0] > lista1[2][1]:
        return  'prossiga'