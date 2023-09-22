def carros(p,c,d):
    """calcula e retorna a quantidade de carros necessários para a viagem dados 
    o número de passageiros P e a capacidade convencional C
    e a não convencional D"""
    return p//c+(p-p//c)//d