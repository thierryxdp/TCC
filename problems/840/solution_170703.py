def bolos(farinha,ovos,leite):
    '''Função que diz quantos bolos é possível fazer com base 
    numa receita que usa 2 xícaras de farinha, 3 ovos e 5 colheres
    de sopa de leite'''
    return min((farinha//2),(ovos//3),(leite//5))