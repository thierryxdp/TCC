def bolos(farinha, ovos, leite):
    '''a funcao recebe como parametos [farinha, ovos, leite] 
    e ve quantas divisoes possiveis sao de acordo com o preescrito na receita
    retornando o menor valor possivel de se formar com um dos ingredientes'''
    return min(farinha//2, ovos//3, leite//5)