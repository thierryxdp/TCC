def pontos_por_time(lista):
    '''Função que recebe uma lista de dois elementos 
    (esses elementos por sua vez também são listas,jogo de ida
    e jogo de volta) e retornam o time e seus respectivos pontos.
    valores: list ---> dicionario'''
    pontosA=0
    pontosB=0
    if lista[0][2][0] > lista[0][2][1]:
    	pontosA= pontosA+3
    if lista[1][2][1] > lista[1][2][0]:
        pontosA= pontosA+3
    if lista[0][2][0] == lista[0][2][1]:
        pontosA= pontosA+1  
        pontosB= pontosB+1
    if lista[1][2][0] == lista[1][2][1]:
        pontosA= pontosA+1  
        pontosB= pontosB+1
    if lista[0][2][1] > lista[0][2][0]:
        pontosB= pontosB+3
    if lista[1][2][0] > lista[1][2][1]:
        pontosB= pontosB+3
    return {lista[0][0]: pontosA, lista[0][1]: pontosB}